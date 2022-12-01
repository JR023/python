from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojo:
    def __init__ (self, data):
        self.id = data ["id"]
        self.name =data ["name"]
        self.created_at = data ["created_at"]
        self.updated_at = data ["updated_at"]

    @classmethod
    def create_dojo(cls,data):
        query = "insert into dojos(name)"
        query += "values(%(name)s);"
        result = connectToMySQL (DATABASE).query_db(query,data)
        return result
    
    @classmethod
    def get_dojo(cls):
        query = "select * from dojos;"
        result = connectToMySQL(DATABASE).query_db(query)
        dojo_db = []
        for row in result:
            dojo_db.append (cls(row))
        return dojo_db