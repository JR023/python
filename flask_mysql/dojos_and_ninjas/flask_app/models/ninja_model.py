from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data  ["first_name"]
        self.last_name = data ["last_name"]
        self.age = data ["age"]
        self.dojo_id = data["dojo_id"]
        self.created_at = data ["created_at"]
        self.updated_at = data ["updated_at"]

    @classmethod
    def create_ninja (cls, data):
        query = "insert into ninjas (first_name, last_name, age, dojo_id)"
        query += "values(%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        return result

    @classmethod
    def get_ninja(cls):
        query = "select * from ninjas;"
        result = connectToMySQL ("dojos_and_ninjas").query_db(query)
        ninja_db = []
        for row in result:
            ninja_db.append(cls(row))
        return ninja_db

    @classmethod
    def get_all_ninja(cls,data):
        query = "select * from ninjas where dojo_id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        ninjas = []
        for row in result:
            ninjas.append(cls(row))
        return ninjas