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
    cursor.execute('SELECT username FROM member;')
    used_username = cursor.fetchall()
    cursor.close()
    conn.close()
    for i in range(len(used_username)):
        if username == used_username[i][0]:
            return redirect('/error?message=帳號已被註冊')
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO member (name, username, password) Values(\'{name}\', \'{username}\', \'{password}\')')
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')


# 登入 POST
@app.route('/signin', methods = ['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, username, password FROM member')
    member_info = cursor.fetchall()
    cursor.close()
    conn.close()
    for i in range(len(member_info)):
        if username == member_info[i][2] and password == member_info[i][3]:
            session['login'] = True
            session['id'] = member_info[i][0]
            session['username'] = member_info[i][2]
            session['name'] = member_info[i][1]
            return redirect('/member')
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
    cursor.execute('SELECT member.name, message.content FROM message INNER JOIN member ON message.member_id=member.id ORDER BY message.time DESC;')
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps(messages)

# 新增留言
@app.route('/createMessage', methods = ['POST'])
def create_message():
    content = request.form['content']
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO message(member_id, content) VALUES(\'{session["id"]}\', \'{content}\');')
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