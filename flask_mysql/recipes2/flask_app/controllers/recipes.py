from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

#use in dashboard to create initial recipe
@app.route('/new/recipe')
def new_recipe():
#validate user session
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_recipe.html',user=User.get_by_id(data))

#use in new_recipe to store submission to database
@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    #validate user login
    if 'user_id' not in session:
        return redirect('/logout')
    #validate ample characters
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "user_id": session["user_id"]
    }
    Recipe.save(data)
    #after completing submissin return to dashboard
    return redirect('/dashboard')
#use for dashboard to get recipe id for right user and route to edit recipe html
@app.route('/edit/recipe/<int:id>')
def edit_recipe(id):
    #validate user session
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html",edit=Recipe.get_one(data),user=User.get_by_id(user_data))

#use in edit_recipe to update database
@app.route('/update/recipe',methods=['POST'])
def update_recipe():
    #validate user session
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.validate_recipe(request.form):
        return redirect('/new/recipe')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under30": int(request.form["under30"]),
        "date_made": request.form["date_made"],
        "id": request.form['id']
    }
    Recipe.update(data)
    #return dashboard after completion
    return redirect('/dashboard')

#use in dashboard to route to recipe id
@app.route('/recipe/<int:id>')
def show_recipe(id):
    #validate user session
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_recipe.html",recipe=Recipe.get_one(data),user=User.get_by_id(user_data))

#delete recipe
@app.route('/destroy/recipe/<int:id>')
def destroy_recipe(id):
    #validate user session
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Recipe.destroy(data)
    return redirect('/dashboard')