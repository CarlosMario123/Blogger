from db.db import Database
class Followers:
    def __init__(self):
        self.bd = Database()
    
    def verSiguiendo(self, id_user):
        try:
            connection = self.bd.get_connection()
            cursor = connection.cursor()
        
        # Evitar la vulnerabilidad de la inyección SQL
            query = "select * from usuario inner join follow on usuario.id_usuario = follow.siguiendo where seguidor =%s;"
            cursor.execute(query, (id_user,))
        
        # Recuperar los resultados de la consulta
            follows = cursor.fetchall()
            print(follows[0][1])
            return follows
        except Exception as e:
            print("Error al obtener los usuarios seguidos:", e)
            return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


        