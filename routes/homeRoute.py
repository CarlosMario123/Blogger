from flask import render_template, request, redirect, url_for, flash, Blueprint

from auth.authDecorator import token_required


homeRoute = Blueprint("home", __name__)

@homeRoute.route("/", methods=["GET", "POST"])
@token_required
def index():
   return render_template("home/index.html")
    

