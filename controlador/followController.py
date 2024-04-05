from flask import jsonify
from db.db import Database
class FollowController:
    def __init__(self):
        self.bd = Database()
    def seguir(self,seguidor,siguiendo):
        try:
            connection = self.bd.get_connection()
            cursor = connection.cursor()
            query = "insert into follow (seguidor, siguiendo) VALUE (%s, %s)"
            cursor.execute(query, (seguidor,siguiendo))
            connection.commit() 
            return True
        except Exception as e:
            print(e)
            return False
