from flask import Blueprint,jsonify
flowRoute = Blueprint("follow", __name__)
from controlador.followController import FollowController
from auth.authDecorator import token_required
followController = FollowController()

@flowRoute.route("/seguir/<int:id_seguidor>/<int:id_usuario_a_seguir>/", methods=["POST"])
@token_required
def seguir(id_seguidor, id_usuario_a_seguir):
    print(id_seguidor,id_usuario_a_seguir)
    value = followController.seguir(id_seguidor,id_usuario_a_seguir)
    return jsonify({"success":value})
    
    
