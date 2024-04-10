from routes.authRoute import authRoute
from routes.homeRoute import homeRoute
from routes.followRoute import flowRoute
from routes.publishRoute import publishRoute

def instanceRoute(app):
    app.register_blueprint(homeRoute)
    app.register_blueprint(authRoute,url_prefix='/auth')
    app.register_blueprint(flowRoute,url_prefix='/follow')
    app.register_blueprint(publishRoute,url_prefix='/publish')
    