from flask import Flask

app = Flask(__name__)

DATABASE= 'dojos_and_ninjas'

app.secret_key = "shhhhhh"