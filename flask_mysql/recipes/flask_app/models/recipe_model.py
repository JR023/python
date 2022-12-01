from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app import DATABASE

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.user_id = data['user_id']

    @classmethod
    def new_recipe(cls, data):
        query = 'INSERT INTO recipes (name, under_30, description, instruction, date_made, user_id)'
        query += 'VALUES (%(name)s, %(under_30)s, %(description)s, %(instruction)s, %(date_made)s, %(user_id)s);'
        result = connectToMySQL(DATABASE).query_db(query,data)
        return result

    @classmethod
    def get_all_recipes(cls):
        query = 'SELECT * FROM recipes;'
        result = connectToMySQL (DATABASE).query_db(query)
        recipes = []
        for row in result:
            recipes.append(cls(row))
        return recipes

    @classmethod
    def get_one_recipe (cls,data):
        query = 'SELECT * FROM recipes WHERE id=%(id)s;'
        result = connectToMySQL (DATABASE).query_db(query,data)
        return cls(result[0])

    @classmethod
    def edit_recipe (cls,data):
        query = "UPDATE recipes SET name = %(name)s, under_30 = %(under_30)s, description = %(description)s,"
        query += "instructions = %(instructions)s, date_made = %(date_made)s, updated_at = NOW() WHERE id= %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod
    def delete (cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid= True 
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid=False

        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid=False

        if len(recipe['instructions']) < 3:
            flash("Instruction must be at least 3 characters.")
            is_valid=False
        return is_valid