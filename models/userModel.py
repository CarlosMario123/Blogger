from db.db import Database
class UserModel:
    def __init__(self):
        self.bd = Database()
    def findUserByEmail(self,email):
        try:
            connection = self.bd.get_connection()
            cursor = connection.cursor()
            # para Evita la vulnerabilidad de inyección SQL 
            query = "SELECT * FROM usuario WHERE correo = %s"
            cursor.execute(query, (email,))
             #we use % to avoid sql injection attack
            user = cursor.fetchone()
            return user[0]
        except Exception as e:
            return -1
            
            
        
    