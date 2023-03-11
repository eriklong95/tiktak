from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.get('/')
    def welcome():
        return '<h1>Welcome to tiktak</h1>'
    
    from . import api
    app.register_blueprint(api.bp)

    return app