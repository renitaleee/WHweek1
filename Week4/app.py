from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = '2000915'

# 首頁
@app.route('/')
def home_page():
    return render_template('homePage.html')    

# 登入 POST
@app.route('/signin', methods = ['POST'])
def sign_in():
    account = request.form['account']
    password = request.form['password']
    if account == 'test' and password == 'test':
        session['login'] = True
        return redirect('/member')
    elif account == '' or password == '':
        return redirect('/error?message=請輸入帳號、密碼')
    else:
        return redirect('/error?message=帳號、密碼輸入錯誤')

# 會員畫面
@app.route('/member')
def member():
    if session['login'] == True:
        return render_template('member.html')
    else:
        return redirect('/')

# 登出系統並跳回首頁
@app.route('/signout')
def sign_out():
    session['login'] = False
    return redirect('/')

# 失敗頁面
@app.route('/error')
def error():
    error_message = request.args.get('message','')
    return render_template('error.html', message = error_message)

# 將數字平方
@app.route('/square')
def get_square():
    num = request.args.get('number','')
    return redirect('/square/'+num)

@app.route('/square/<num>')
def cal(num):
    square = int(num) ** 2
    return render_template('square.html', squareNum = square)

app.run(port=3000)