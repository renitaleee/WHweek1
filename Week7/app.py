from flask import Flask, render_template, session, redirect, request, jsonify
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
    cursor.execute('SELECT id, name, username, password FROM member WHERE username=%s AND password=%s',signin_data)
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
    try:
        if session['login'] == True:
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute('SELECT message.id, member.username, member.name, message.content FROM message INNER JOIN member ON message.member_id=member.id ORDER BY message.time DESC;')
            messages = cursor.fetchall()
            cursor.close()
            conn.close()
            messages.append(session['username'])
            return json.dumps(messages)
    except:
        return redirect('/')

# 新增留言
@app.route('/createMessage', methods = ['POST'])
def create_message():
    try:
        if session['login'] == True:
            content = request.form['content']
            message_data = (session['id'], content)
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO message(member_id, content) VALUES(%s, %s);', message_data)
            conn.commit()
            cursor.close()
            conn.close()
            return redirect('/member')
    except:
        return redirect('/')

# 刪除留言
@app.route('/deleteMessage', methods = ['POST'])
def del_message():
    try:
        if session['login'] == True:
            message_id = request.form['messageID']
            conn = connect_to_db()
            cursor = conn.cursor()
            cursor.execute('SELECT member_id FROM message WHERE id=%s',(message_id,))
            record = cursor.fetchone()
            if record[0] == session['id']:
                cursor.execute('DELETE FROM message WHERE id=%s', (message_id,))
                conn.commit()
            cursor.close()
            conn.close()
            return redirect('/member')
    except:
        return redirect('/')

# 查詢/修改會員姓名
@app.route('/api/member', methods = ['GET', 'PATCH'])
def member_api():
    if request.method == 'GET':
        try:
            if session['login'] == True:
                search_username = request.args.get('username', None)
                conn = connect_to_db()
                cursor = conn.cursor()
                cursor.execute('SELECT id, name, username from member WHERE username=%s', (search_username,))
                record = cursor.fetchone()
                cursor.close()
                conn.close()
                if record:
                    member_data = {
                    'data':{
                        'id':record[0],
                        'name':record[1],
                        'username':record[2]
                        }
                    }
                    return jsonify(member_data)
                else:
                    return jsonify({'data':None})
        except:
            return jsonify({'data':None})
    elif request.method == 'PATCH':
        try:
            if session['login'] == True:
                new_name = request.json.get('name')
                conn = connect_to_db()
                cursor = conn.cursor()
                cursor.execute('UPDATE member SET name=%s WHERE id=%s',(new_name,session['id']))
                conn.commit()
                cursor.close()
                conn.close()
                session['name'] = new_name
                return jsonify({'ok': True})
        except:
            return jsonify({'error': True})
    

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