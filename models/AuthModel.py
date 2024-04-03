from db.db import Database
from utils.hashPasword import hash_password,verify_password
class AuthModel:
    def __init__(self):
        self.bd = Database()
        
    
    def createUser(self,email,password):
        if self.verifyExist(email):
            return False
        try:
            connection = self.bd.get_connection()
            cursor = connection.cursor()
            hashed_password = hash_password(password)
            query = "INSERT INTO usuario (correo,password) VALUES (%s, %s)"
            cursor.execute(query, (email, hashed_password))
            #confirm the transaction
            connection.commit() 
            return True
        except Exception as e:
            print("Errror: ",e)
            return False
            
        
        
    def verifyExist(self,email):#verify that the user exists
        try:
            connection = self.bd.get_connection()
            cursor = connection.cursor()
            # para Evita la vulnerabilidad de inyección SQL 
            query = "SELECT * FROM usuario WHERE correo = %s"
            cursor.execute(query, (email,))
        
             #we use % to avoid sql injection attack
            user = cursor.fetchone()
            
            if user:
                return True
            return False #not find the user
        except Exception as e:
            print("Error: ",e)
            print("Error:", e)
        finally:
            cursor.close()
            connection.close()
            
    def Logearse(self, email, password):
        try:
            connection = self.bd.get_connection()
            cursor = connection.cursor()
            # Consulta SQL para obtener la contraseña hasheada del usuario
            query = "SELECT password FROM usuario WHERE correo = %s"
            cursor.execute(query, (email,))
            stored_password = cursor.fetchone()
            
            if not stored_password:
                return False  # Si el usuario no existe, devuelve False
            
            # Verifica la contraseña hasheada con la proporcionada
            if verify_password(stored_password[0], password):
                
                return True 
            else:
                return False  # Si la contraseña no coincide, devuelve False
        except Exception as e:
            print("Error:", e)
            return False
        finally:
            cursor.close()
            connection.close()

          
                             
        