from routes.authRoute import authRoute
from routes.homeRoute import homeRoute

def instanceRoute(app):
    app.register_blueprint(homeRoute)
    app.register_blueprint(authRoute,url_prefix='/auth')