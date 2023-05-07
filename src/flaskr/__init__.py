from logging import config
from flask import Flask, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from src.flaskr.persistence.db_connection.db_connection_supplier import DatabaseConnectionSupplier


def create_app():
    # read config

    config.dictConfig({
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

    initialize_database(app.logger)

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


def initialize_database(logger):
    logger.info('Initializing database')

    connection = DatabaseConnectionSupplier().get()
    cursor = connection.cursor()

    all_tables_result = cursor.execute('SELECT name FROM sqlite_master')
    tables = all_tables_result.fetchall()

    user_table_exists = any(list(filter(lambda t: t[0] == 'user', tables)))
    if not user_table_exists:
        cursor.execute('CREATE TABLE user(username, rank)')
        logger.info('Created table \'user\'')

    game_table_exists = any(list(filter(lambda t: t[0] == 'game', tables)))
    if not game_table_exists:
        cursor.execute('CREATE TABLE game(id, player_a, player_b)')
        logger.info('Created table \'game\'')
