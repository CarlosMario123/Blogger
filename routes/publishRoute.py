from flask import Blueprint,request,jsonify
from flask_jwt_extended import get_jwt_identity
from controlador.publishController import PublishController
from auth.authDecorator import token_required
publishRoute = Blueprint("publish", __name__)

publishController = PublishController()
@publishRoute.route("/",methods=["POST"])
@token_required
def create():
    datos_json = request.json #recibimos los datos en json
    user = get_jwt_identity()
    result = publishController.createPublish(datos_json,user)
    
    if result:
        return jsonify({"Msg":"post created successfully"})
    return jsonify({"msg":"error creating post"})
    
    
