from flask import Flask
from flask_jwt_extended import JWTManager
from routes.allRoutes import instanceRoute


app = Flask(__name__)
app.secret_key = "clave123"
#Configuracion de cookies junto con jwt
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_SECRET_KEY'] = 'clave123' 
jwt = JWTManager(app)

instanceRoute(app)
if __name__ == '__main__':
    app.run(debug=True)