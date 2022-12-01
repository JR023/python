from flask_app import app
from flask_app.controllers import dojo_controller, ninja_controller

#this needs to be at the bottom
if __name__=="__main__":
    app.run(debug=True)