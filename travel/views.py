from flask import Blueprint, render_template, request, session
mainbp = Blueprint ('main',__name__)

@mainbp.route('/')
def index():
    return render_template('index.html')

@mainbp.route('/login')
def login():
    email = request.values.get("email")
    passwd = request.values.get("pwd")
    print (f"Email: {email}\nPassword: {passwd}")
    #store email in session
    session['email'] = request.values.get('email')
    return render_template('login.html')

@mainbp.route('/logout')
def logout():
    if 'email' in session:
        session.pop('email')
    return 'User logged out'
