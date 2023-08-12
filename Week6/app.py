from flask import Flask, render_template, session, redirect, request
import mysql.connector
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = '2000915'

def connect_to_db():
    load_dotenv()
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'website',
        user = os.getenv('user'),
        password = os.getenv('password')
    )
    return conn

# 首頁
@app.route('/')
def home_page():
    return render_template('homePage.html')

# 註冊 POST
@app.route('/signup', methods = ['POST'])
def signup():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    conn = connect_to_db()
    cursor = conn.cursor()
    check_data = (username,)
    cursor.execute('SELECT username FROM member WHERE username=%s;',check_data)
    used_username = cursor.fetchone()
    cursor.close()
    conn.close()
    if used_username:
        return redirect('/error?message=帳號已被註冊')
    conn = connect_to_db()
    cursor = conn.cursor()
    sign_up_data = (name, username, password)
    cursor.execute('INSERT INTO member (name, username, password) Values(%s, %s, %s);', sign_up_data)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


# 登入 POST
@app.route('/signin', methods = ['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    signin_data = (username, password)
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, username, password FROM member WHERE username=%s AND password=%s;', signin_data)
    member_info = cursor.fetchone()
    cursor.close()
    conn.close()
    if member_info:
        session['login'] = True
        session['id'] = member_info[0]
        session['name'] = member_info[1]
        session['username'] = member_info[2]
        return redirect('/member')
    else:
        return redirect('/error?message=帳號或密碼輸入錯誤')
    

# 會員畫面
@app.route('/member')
def member():
    try:
        if session['login'] == True:
            return render_template('member.html', name = session['name'])
    except:
        return redirect('/')
    
# 取得留言
@app.route('/getmessage')
def get_message():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT message.id, member.username, member.name, message.content FROM message INNER JOIN member ON message.member_id=member.id ORDER BY message.time DESC;')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    messages.append(session['username'])
    return json.dumps(messages)

# 新增留言
@app.route('/createMessage', methods = ['POST'])
def create_message():
    content = request.form['content']
    message_data = (session['id'], content)
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO message(member_id, content) VALUES(%s, %s);', message_data)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/member')

# 刪除留言
@app.route('/deleteMessage', methods = ['POST'])
def del_message():
    message_id = request.form['messageID']
    message_id = (message_id,)
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM message WHERE id=%s', message_id)
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/member')
    

# 登出系統並跳回首頁
@app.route('/signout')
def sign_out():
    session.clear()
    return redirect('/')

# 失敗頁面
@app.route('/error')
def error():
    error_message = request.args.get('message','')
    return render_template('error.html', message = error_message)

app.run(port=3000)