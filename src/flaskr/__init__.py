from flask import Flask, redirect, url_for
from flask_swagger_ui import get_swaggerui_blueprint
from logging.config import dictConfig


def create_app():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        }
    })

    app = Flask(__name__)

    @app.get('/')
    def index():
        return redirect('/static/index.html', 302)

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
    app.register_blueprint(api.bp, url_prefix='/api')

    return app
