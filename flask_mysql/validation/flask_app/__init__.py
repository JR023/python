from flask import Flask
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.secret_key = "4f7123f5-cc7a-4d24-827e-b9030b650e72"

DATABASE = 'login_db'

bcrypt = Bcrypt(app)