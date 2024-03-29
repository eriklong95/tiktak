from flask import jsonify, make_response
import src.flaskr.controllers.turn_logic as turn_logic
from src.flaskr.controllers.uuid_supplier import UuidSupplier
import src.flaskr.controllers.winner_logic as winner_logic
from src.flaskr.models.game_model import Game, GameSchema, MoveSchema
from src.flaskr.persistence.repositories.game_repository_api import GameRepositoryApi


GAME_SCHEMA = GameSchema()
MOVE_SCHEMA = MoveSchema()


def games__get__list(request):
    # This is how you get the value of the query param
    # with key 'username'. Returns None if no value passed
    username = request.args.get('username')

    repo = GameRepositoryApi()
    games = repo.select_all_games()

    if username == None:
        return make_response([g.id for g in games], 200)
    
    filtered_games = [g for g in games if g.player_a == username or g.player_b == username]

    return make_response([g.id for g in filtered_games], 200)


def games__post__create(request):
    # creates a new game object based on the data in the request
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

    if (game == None):
        return make_response('No game with this ID was found on the server.', 404)
    
    return make_response(GAME_SCHEMA.dump(game), 200)
    

def some_game__get__turn(request, game_id):
    repo = GameRepositoryApi()
    game = repo.select_game(game_id)

    if game is None:
        return make_response('No game with ID ' + game_id, 404)

    turn = turn_logic.derive_turn(game)
    return make_response(jsonify(turn), 200)
   

def some_game__get__winner(request, game_id):
    repo = GameRepositoryApi()
    game = repo.select_game(game_id)

    if game is None:
        msg = 'No game with this ID was found on the server.'
        return make_response(msg, 404)
    
    status = winner_logic.find_winner(game)

    return make_response(jsonify(status), 200)


def some_game__post__move(request, game_id):
    # gets the request body and deserializes it into a Move model object
    body = request.json
    move = MOVE_SCHEMA.load(body)

    if not (move.x in [0,1,2] and move.y in [0,1,2]):
        msg = 'Invalid move coordinates.'
        return make_response(msg, 400)

    repo = GameRepositoryApi()
    game = repo.select_game(game_id)

    if game is None:
        msg = 'No game with this ID was found on the server.'
        return make_response(msg, 404)

    turn = turn_logic.derive_turn(game)

    is_occupied = len([m for m in game.moves if m.x == move.x and m.y == move.y]) > 0
    is_game_decided = winner_logic.find_winner(game) != 'undecided'
    is_invalid_move = turn != move.occupier or is_occupied or is_game_decided
    if (is_invalid_move):
        msg = 'Illegal move. This player does not have the turn or this field is already occupied.'
        return make_response(msg, 403)
    
    repo.insert_move(move, game_id)
    repo.commit()

    updated_game = repo.select_game(game_id)

    return make_response(GAME_SCHEMA.dump(updated_game), 201)
