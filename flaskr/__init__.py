from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)

    @app.get('/')
    def welcome():
        return '<h1>Welcome to tiktak</h1>'
    
    @app.get('/api')
    def api_documentation():
        # redirect to openapi documentation
        return redirect(url_for('static', filename='openapi.json'), code=302)
    
    from . import api
    app.register_blueprint(api.bp)

    return app