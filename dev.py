#esto fue una prueba para probar si funciona con waitres
from flask import Flask
from flask_jwt_extended import JWTManager
from routes.allRoutes import instanceRoute
from waitress import serve  # Importa serve de Waitress

app = Flask(__name__)
app.secret_key = "clave123"
# Configuración de cookies junto con JWT
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
app.config['JWT_SECRET_KEY'] = 'clave123'
jwt = JWTManager(app)

instanceRoute(app)

if __name__ == '__main__':
    # Ejecuta el servidor Waitress
    serve(app, host='0.0.0.0', port=5000)
