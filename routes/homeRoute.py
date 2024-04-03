from flask import render_template, request, redirect, url_for, flash,Blueprint
from flask_jwt_extended import  jwt_required


homeRoute = Blueprint("home", __name__)

@homeRoute.route("/",methods = ["GET","POST"])
@jwt_required()
def index():
    return "ff"