#import the function that will return an instance of a connection
from cmath import log
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, bcrypt
from flask import flash, session


import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

#model the class after the friend table from our database
class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw = data['pw']


    @property
    def fullname(self):
        return f"{self.first_name}{self.last_name}"

    #C
    @classmethod
    def create(cls, data:dict) -> int:
        query = "INSERT INTO users (first_name, last_name, email, pw) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    #R
    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM users WHERE id= %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_one_by_email(cls, data:dict) -> list:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_all(cls) -> list:
        query = "Select * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return False
    
    #U
    @classmethod
    def update_one(cls, data:dict) -> None:
        query = "UPDATE users SET first_name = %(first_name)s WHERE id = %(id)s;"
        return connectToMySQL (DATABASE).query_db(query,data)

    #D
    @classmethod
    def delete_one(cls, data:dict) -> None:
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def registration_validator(form_data):
        is_valid = True

        if len(form_data['first_name'])<1:
            is_valid = False
            flash('First name is required', 'err_users_first_name')

            
        if len(form_data['last_name'])<1:
            is_valid = False
            flash('Last name is required', 'err_users_last_name')

            
        if len(form_data['email'])<1:
            is_valid = False
            flash('Email is required', 'err_users_email')
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", 'err_users_email')
            is_valid = False
        else:
            potential_user = User.get_one_by_email({'email': form_data['email']})
            if potential_user:
                flash("Email already in use!", 'err_users_email')
                is_valid= False

            
        if len(form_data['pw'])<1:
            is_valid = False
            flash("Password is required", 'err_users_pw')

            
        if len(form_data['confirm_pw'])<1:
            is_valid = False
            flash('Confirm Password is required', 'err_users_confirm_pw')
        elif form_data['pw'] != form_data['confirm_pw']:
            is_valid = False
            flash("Passwords do not match", 'err_users_confirm_pw')
        return is_valid

    @staticmethod
    def login_validator(form_data):
        is_valid = True
        if len(form_data['email'])<1:
            is_valid = False
            flash('Email is required', 'err_users_email_login')
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!", 'err_users_email_login')
            is_valid = False

            
        if len(form_data['pw'])<1:
            is_valid = False
            flash('Password is required', 'err_users_pw_login')
        if is_valid:
            potential_user = User.get_one_by_email({'email':form_data['email']})
            if not bcrypt.check_password_hash(potential_user.pw, form_data['pw']):
                is_valid = False
                flash('Invalid Credentials', 'err_users_pw_login') 
            else:
                session['uuid'] = potential_user.id
            #check bcrypt
        return is_valid