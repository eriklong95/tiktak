from flask import jsonify, make_response
import src.flaskr.controllers.turn_logic as turn_logic
from src.flaskr.controllers.uuid_supplier import UuidSupplier
import src.flaskr.controllers.winner_logic as winner_logic
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
        turn = turn_logic.derive_turn(game)
        return make_response(jsonify(turn), 200)
    except:
        return make_response(500)


def some_game__get__winner(request, game_id):
    repo = GameRepositoryApi()
    game = repo.select_game(game_id)

    if game is None:
        return make_response('No game with ID ' + game_id, 404)
    else:
        winner = winner_logic.find_winner(game)
        return make_response(jsonify(winner), 200)


def some_game__post__move(request, game_id):
    body = request.json
    move = MOVE_SCHEMA.load(body)
    player = move.occupier
    repo = GameRepositoryApi()

    game = repo.select_game(game_id)

    if game is None:
        return make_response('No game with ID ' + game_id, 404)
    
    turn = turn_logic.derive_turn(game)

    if not turn == move.occupier:
        return make_response('Player ' + player + ' does not have the turn', 403)

    repo.insert_move(move, game_id)
    repo.commit()
    return make_response('Move successfully inserted', 201)
