from functools import wraps
from flask import redirect, url_for
from flask_jwt_extended import verify_jwt_in_request

def token_required(fn):
    @wraps(fn)
    def decorated_function(*args, **kwargs):
        try:
            # Verificar si el token JWT está presente y es válido
            verify_jwt_in_request()
        except Exception as e:
            # Si se produce una excepción relacionada con el token JWT, manejarla aquí
            print("Error verificando token JWT:", e)  # Agrega un registro de depuración
            return redirect(url_for("auth.inicio"))
        
        # Si el token es válido, ejecutar la función original
        return fn(*args, **kwargs)
    
    return decorated_function

    
    return decorated_function