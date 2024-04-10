from utils.verifyJson import verificarCamposJson
from models.userModel import UserModel
from repositorios.publicacionRepository import PublishRepository
from models.publicacionModel import PublicacionModel
class PublishController:
    def createPublish(self,data,email):
        isEnter =  verificarCamposJson(data,["contenido"])
        
        if isEnter:
            try:
                userModel = UserModel()
                idUser = userModel.findUserByEmail(email)
                publish = PublishRepository()
                
                publish.createPublish(PublicacionModel(idUser,data["contenido"]))
                return True
            except Exception as e:
                print("Error...........")
                print(e)
                return False
        return False    
            
            
            