from flask import render_template, request, redirect, url_for, flash,Blueprint,jsonify
from flask_jwt_extended import create_access_token,set_access_cookies

from controlador.authController import AuthContoller
authRoute = Blueprint("auth", __name__,url_prefix='/auth')
authController = AuthContoller()

@authRoute.route("/login/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        if request.is_json:  # Verificar si se envió JSON
            username = request.json.get("correo")
            password = request.json.get("password")
        else:  # Si no es JSON, se asume que es un formulario HTML
            username = request.form.get("correo")
            password = request.form.get("password")

        isLogin, msg = authController.loging(username, password)

        if isLogin:
            flash(msg)
            usuario = username
            access_token = create_access_token(identity=usuario)
            response = jsonify({"mensaje": "Inicio de sesión exitoso", "token": access_token})
            response.status_code = 200
            response.headers.add('Access-Control-Allow-Origin', '*')
            #Este metodo establece una cookie en la respuesta HTTP que se enviará al cliente.
            response.set_cookie('token', access_token, httponly=True, secure=True)
            set_access_cookies(response, access_token)
            return response

        flash(msg)
        return redirect(url_for(".inicio"))

    return render_template("login.html")

#register    
@authRoute.route("/register/",methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['correo']
        password = request.form['password']
        created, message, category = authController.createUser(username,password)
        
        if created:
            flash(message, category)
            return redirect(url_for(".inicio"))
        flash(message, category)
        return redirect(url_for('.register'))
    
    return render_template('register.html')
        
        


