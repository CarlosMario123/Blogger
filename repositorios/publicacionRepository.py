from db.db import Database
from models.publicacionModel import PublicacionModel
class PublishRepository:
    def __init__(self):
        self.bd = Database()
    def createPublish(self,publicacion:PublicacionModel):
        try:
            connection = self.bd.get_connection()
            cursor = connection.cursor()
            query = "INSERT INTO publicacion (id_usuario, contenido) VALUES (%s, %s)"
            datoPublish = publicacion.getData()
            cursor.execute(query,datoPublish)
            connection.commit()

            # Cerrar el cursor y la conexión
            cursor.close()
            connection.close()
            
            return True
        except Exception as e:
            print("Error.................")
            print(e)
            return False
                

            
            
        