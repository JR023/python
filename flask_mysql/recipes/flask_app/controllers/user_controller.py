from flask_app import app, bcrypt
from flask import render_template, redirect, session, request, flash

from flask_app.models import user_model
from flask_app.models import recipe_model


@app.route('/')
def index():
    if 'uuid' in session: 
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session:
        return redirect ('/')
    data = {
        'id' : session['uuid']
    }
    user = user_model.User.get_one(data)
    recipes= recipe_model.Recipe.get_all_recipes()
    return render_template('dashboard.html', user=user, recipes=recipes)

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/create', methods=['POST'])
def user_create():
    print(request.form)
    if not user_model.User.registration_validator(request.form):
        return redirect ('/')
    pw_hash = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw': pw_hash
    }
    id = user_model.User.create(data)
    session['uuid'] = id
    return redirect('/dashboard')

@app.route('/user/login', methods=['POST'])
def user_login():
    if not user_model.User.login_validator(request.form):
        return redirect ('/')
    return redirect ('/')

