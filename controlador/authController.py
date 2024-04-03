from models.AuthModel import AuthModel
class AuthContoller:
    def __init__(self):
        self.auth = AuthModel()
    
    def createUser(self, correo, password):
        isCreated = self.auth.createUser(correo, password)
        if isCreated:
            return True, 'Cuenta creada exitosamente. Por favor inicia sesión.', 'success'
        return False, 'El nombre de usuario ya está en uso.', 'error'
    
    def loging(self,correo,password):
        isLogin = self.auth.Logearse(correo,password)
        
        if isLogin:
            return True,"Exitosamente"
        return False, "Error al iniciar seccion intenta de nuevo"
        