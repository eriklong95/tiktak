from flask import Flask, redirect, url_for
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)

    @app.get('/')
    def welcome():
        return '<h1>Welcome to tiktak</h1>'
    
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/openapi.json'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "tiktak"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    from . import api
    app.register_blueprint(api.bp)
    


    return app
