import uuid
from flask import jsonify, make_response
from src.flaskr.models.game_model import Game, GameSchema
from src.flaskr.persistence.repositories.game_repository_api import GameRepositoryApi


GAME_SCHEMA = GameSchema()


def games__get__list(request):
    repo = GameRepositoryApi()
    games = repo.select_all_games()
    return make_response([g.id for g in games], 200)


def games__post__create(request):
    repo = GameRepositoryApi()
    body = request.get_json()
    game = Game(id=str(uuid.uuid4()),
                player_a=body['opponent'], player_b=body['challenger'], moves=[])
    repo.insert(game=game)
    repo.commit()
    return make_response(jsonify(game.id), 201)


def some_game__get__info(request, game_id):
    repo = GameRepositoryApi()
    game = repo.select_game(game_id=game_id)

    if game is None:
        return make_response('No game with ID ' + game_id + ' exists', 404)
    else:
        return make_response(GAME_SCHEMA.dump(game), 200)


def some_game__get__winner(request, game_id):
    return "some_game__get__winner"


def some_game__post__move(request, game_id):
    return "some_game__post__move"
