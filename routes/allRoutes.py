from routes.authRoute import authRoute
from routes.homeRoute import homeRoute
from routes.followRoute import flowRoute

def instanceRoute(app):
    app.register_blueprint(homeRoute)
    app.register_blueprint(authRoute,url_prefix='/auth')
    app.register_blueprint(flowRoute,url_prefix='/follow')
    