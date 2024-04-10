from flask import jsonify
from db.db import Database
from models.userModel import UserModel
from models.followers import Followers
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
    def viewFollowers(self,email):
        userModel = UserModel()
        followers = Followers()
        idUser = userModel.findUserByEmail(email)
        return followers.verSiguiendo(idUser)
        