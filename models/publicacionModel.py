class PublicacionModel:
    def __init__(self, id_usuario, contenido):
        self.id_usuario = id_usuario
        self.contenido = contenido
    
    def getData(self):
        return (self.id_usuario, self.contenido)    