from flask import Blueprint,jsonify,render_template
from flask_jwt_extended import get_jwt_identity
from controlador.followController import FollowController
from auth.authDecorator import token_required
flowRoute = Blueprint("follow", __name__)
followController = FollowController()

@flowRoute.route("/", methods=["GET"])
@token_required
def followers():
  
    user = get_jwt_identity()
    followers = followController.viewFollowers(user)
    return render_template("home/friends.html", followers=followers)

@flowRoute.route("/seguir/<int:id_seguidor>/<int:id_usuario_a_seguir>/", methods=["POST"])
@token_required
def seguir(id_seguidor, id_usuario_a_seguir):
    value = followController.seguir(id_seguidor,id_usuario_a_seguir)
    return jsonify({"success":value})



    
    
    
