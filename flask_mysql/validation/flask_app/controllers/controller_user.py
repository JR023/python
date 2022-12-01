from flask_app import app, bcrypt
from flask import render_template, redirect, session, request

from flask_app.models import model_user

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/create', methods=['POST'])
def user_create():
    print(request.form)
    if not model_user.User.registration_validator(request.form):
        return redirect ('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw': pw_hash
    }
    id = model_user.User.create(data)
    session['uuid'] = id
    return redirect('/')

@app.route('/user/login', methods=['POST'])
def user_login():
    if not model_user.User.login_validator(request.form):
        return redirect ('/')
    return redirect ('/')

