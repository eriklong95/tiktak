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
    
    return make_response(id, 201)


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

    try:
        turn = turn_logic.derive_turn(game)
        return make_response(jsonify(turn), 200)
    except:
        return make_response(500)


def some_game__get__winner(request, game_id):
    # TODO: implement operation
    
    return make_response('Not yet implemented', 500)


def some_game__post__move(request, game_id):
    # gets the request body and deserializes it into a Move model object
    body = request.json
    move = MOVE_SCHEMA.load(body)

    # TODO: Insert move into correct game

    return make_response('Not yet implemented', 500)
