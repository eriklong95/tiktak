from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)

    @app.get('/')
    def welcome():
        return '<h1>Welcome to tiktak</h1>'
    
    @app.get('/api')
    def api_documentation():
        return redirect(url_for('static', filename='openapi.json'), code=302)
    
    from . import api
    app.register_blueprint(api.bp)

    return app


if __name__ == '__main__':
    print('Running tests...')
    from flaskr.test.model_test import test_user_model
    test_user_model()