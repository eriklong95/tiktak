import uuid
from flask import jsonify, make_response
from src.flaskr.models.game_model import Game, GameSchema
from src.flaskr.persistence.repositories.game_repository_api import GameRepositoryApi


GAME_SCHEMA = GameSchema()


def games__get__list(request):
    return 'games__get__list'


def games__post__create(request):
    return 'games__post__create'


def some_game__get__info(request, game_id):
    return 'some_game__get__info'


def some_game__get__winner(request, game_id):
    return 'some_game__get__winner'


def some_game__post__move(request, game_id):
    return 'some_game__post__move'
