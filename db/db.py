import mysql.connector
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        load_dotenv()
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")

        self.db_config = {
            "host": self.db_host,
            "user": self.db_user,
            "password": self.db_password,
            "database": self.db_name,
        }

        self.create_tables()

    def get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def create_tables(self):
        connection = self.get_connection()
        cursor = connection.cursor()

        usuario = """
        CREATE TABLE IF NOT EXISTS usuario (
            id_usuario INT PRIMARY KEY AUTO_INCREMENT,
            correo VARCHAR(50) NOT NULL,
            password  VARCHAR(50) NOT NULL
        )
        """
        
        follow = """
        CREATE TABLE IF NOT EXISTS follow (
    seguidor INT,
    siguiendo INT,
    UNIQUE (seguidor, siguiendo),
    FOREIGN KEY (seguidor) REFERENCES usuario(id_usuario),
    FOREIGN KEY (siguiendo) REFERENCES usuario(id_usuario)
         )
       """

        cursor.execute(usuario)
        cursor.execute(follow)
    

        connection.commit()
        cursor.close()
        connection.close()