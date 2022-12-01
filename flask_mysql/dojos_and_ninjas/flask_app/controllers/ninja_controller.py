from flask import redirect, render_template, request, redirect
from flask_app import app
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo
from flask_app.controllers import dojo_controller

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_dojo()
    return render_template("ninja.html",  dojos=dojos)

@app.route("/ninjas/create", methods = ["POST"])
def create_ninja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form ["age"],
        "dojo_id" : request.form ["dojo_id"]
}
    Ninja.create_ninja(data)
    print(request.form)
    return redirect("/ninjas")