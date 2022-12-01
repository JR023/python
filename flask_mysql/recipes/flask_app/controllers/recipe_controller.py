#import features to run app
from flask import render_template, request, redirect, flash, session
from flask_app import app
#import models for class/static methods
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User

@app.route('/create_recipe')
def create_recipe():
    #check logged in to view page
    if 'uuid' not in session:
        flash('You must login to view content.')
        return redirect('/')
    # pass user id for recipes to have creator
    user_id = session['uuid']
    return render_template("new_recipe.html", user=user_id)

@app.route('/new_recipe', methods=["POST"])
def submit_new():
    #check all recipe fields are filled in 
    if not Recipe.validate_recipe(request.form):
        return redirect('/new_recipe')
    #if pass validation send to db
    Recipe.new_recipe(request.form)
    #go dashboard after new recipe
    return redirect ('/dashboard')

@app.route ('/edit_recipe/<int:recipe_id>')
def edit_recipe(recipe_id):
    if 'uuid' not in session:
        flash('You must login to edit content.')
        return redirect ('/')
    data = {
        'id' : recipe_id
    }
    recipe = Recipe.get_one_recipe(data)
    return render_template('edit_recipe.html', recipe=recipe)

@app.route('/update/recipe', methods=['POST'])
def send_edit(id):
    if not Recipe.validate_recipe(request.form):
        return redirect(f'/edit_recipe/{id}')
    data = {
        'id':id,
        'name': request.form['name'],
        'under_30': request.form['under_30'],
        'description': request.form['description'],
        'instructions': request.form['instructions']
    }
    Recipe.edit_recipe(data)
    return redirect('/dashboard')

@app.route('/show_recipe/<int:id>')
def show_recipe(id):
    #check if user logged in
    if 'uuid' not in session:
        flash("You must register or login to view content.")
        return redirect ('/')
    data = {
        'id':id
    }
    recipe = Recipe.get_one_recipe(data)
    data = {
        'id': session['uuid']
    }
    user = User.get_one(data)
    return render_template('show_recipe.html', recipe=recipe, user=user)

@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    data = {
        'id' :id
    }
    Recipe.delete(data)
    return redirect('/dashboard')
