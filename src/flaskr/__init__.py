from logging import config
from flask import Flask, make_response, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from src.flaskr.persistence.db_connection.db_connection_supplier import DatabaseConnectionSupplier


def create_app():
    configure_logging()

    app = Flask(__name__)

    initialize_database(app.logger)
    configure_routing(app)

    return app


def configure_logging():
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


def initialize_database(logger):
    logger.info('Initializing database')

    connection = DatabaseConnectionSupplier().get()
    cursor = connection.cursor()

    all_tables_result = cursor.execute('SELECT name FROM sqlite_master')
    tables = all_tables_result.fetchall()

    user_table_exists = any(list(filter(lambda t: t[0] == 'user', tables)))
    if not user_table_exists:
        cursor.execute(
            'CREATE TABLE user(username TEXT PRIMARY KEY, rank INTEGER)')
        logger.info('Created table \'user\'')

    game_table_exists = any(list(filter(lambda t: t[0] == 'game', tables)))
    if not game_table_exists:
        cursor.execute(
            'CREATE TABLE game(id TEXT PRIMARY KEY, player_a TEXT, player_b TEXT, FOREIGN KEY (player_a) REFERENCES user (username), FOREIGN KEY (player_b) REFERENCES user (username))')
        logger.info('Created table \'game\'')

    move_table_exists = any(list(filter(lambda t: t[0] == 'move', tables)))
    if not move_table_exists:
        cursor.execute(
            'CREATE TABLE move(x INTEGER, y INTEGER, occupier TEXT, game_id TEXT, PRIMARY KEY (game_id, x, y), FOREIGN KEY (game_id) REFERENCES game (id) ON DELETE CASCADE)')
        logger.info('Created table \'move\'')


def configure_routing(app):
    @app.get('/')
    def index():
        return redirect('/static/index.html', 302)

    @app.get('/test')
    def test():
        return make_response('You called the tiktak server and had a successful response', 200)

    SWAGGER_URL = '/docs'
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
