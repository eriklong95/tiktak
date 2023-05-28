from flask import jsonify, make_response
from src.flaskr.controllers.turn_logic import derive_turn
from src.flaskr.controllers.uuid_supplier import UuidSupplier
from src.flaskr.controllers.winner_logic import find_winner
from src.flaskr.models.game_model import Game, GameSchema, MoveSchema
from src.flaskr.persistence.repositories.game_repository_api import GameRepositoryApi


GAME_SCHEMA = GameSchema()
MOVE_SCHEMA = MoveSchema()


def games__get__list(request):
    username = request.args.get('username')
    repo = GameRepositoryApi()
    all_games = repo.select_all_games()
    
    if username is None:
        return [g.id for g in all_games]
    else:
        return [g.id for g in all_games if g.player_a == username or g.player_b == username]


def games__post__create(request):
    body = request.json
    id = UuidSupplier().get()
    new_game = Game(id, body['opponent'], body['challenger'], [])
    repo = GameRepositoryApi()
    repo.insert(new_game)
    repo.commit()
    return make_response(jsonify(id), 201)


def some_game__get__info(request, game_id):
    repo = GameRepositoryApi()
    game = repo.select_game(game_id)
    
    if game is None:
        return make_response('No game with ID ' + game_id, 404)
    else:
        return GAME_SCHEMA.dump(game)
    

def some_game__get__turn(request, game_id):
    repo = GameRepositoryApi()
    game = repo.select_game(game_id)

    if game is None:
        return make_response('No game with ID ' + game_id, 404)

    try:
        turn = derive_turn(game)
        return make_response(jsonify(turn), 200)
    except:
        return make_response(500)


def some_game__get__winner(request, game_id):
    repo = GameRepositoryApi()
    game = repo.select_game(game_id)

    if game is None:
        return make_response('No game with ID ' + game_id, 404)
    else:
        winner = find_winner(game)
        return make_response(jsonify(winner), 200)


def some_game__post__move(request, game_id):
    body = request.json
    move = MOVE_SCHEMA.load(body)
    repo = GameRepositoryApi()
    repo.insert_move(move, game_id)
    repo.commit()
    return make_response('Move successfully inserted', 201)
