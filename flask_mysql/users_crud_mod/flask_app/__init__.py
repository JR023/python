# __init__.py
from flask import Flask

app = Flask(__name__)

database= 'users_schema'

app.secret_key = "shhhhhh"
