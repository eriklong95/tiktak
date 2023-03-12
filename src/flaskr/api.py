# This is generated source code. DO NOT EDIT!
from flask import Blueprint, request
import src.flaskr.controllers.users_controller as users_controller
import src.flaskr.controllers.rank_controller as rank_controller
import src.flaskr.controllers.games_controller as games_controller

bp = Blueprint('api', __name__)
@bp.get('/users')
def users__get__list():
    """Returns a list of all users that have been created on the server."""
    return users_controller.users__get__list(request)


@bp.post('/users')
def users__post__create():
    """Creates a new user on the server with the data provided if a user with this data does not already exist. Returns the user created if successful."""
    return users_controller.users__post__create(request)


@bp.get('/users/{username}')
def some_user__get__info():
    """Returns the basic info about a user with the given username if such a user exists"""
    return users_controller.some_user__get__info(request)


@bp.get('/users/{username}/rank')
def rank__get():
    """Returns the rank for the user with the given username in the form of an integer if such a user can be found on the server"""
    return rank_controller.rank__get(request)


@bp.post('/users/{username}/rank')
def rank__post__change():
    """Change the rank of the user with the given username (if such a user exists) by adding the value if the request body to user's current rank"""
    return rank_controller.rank__post__change(request)


@bp.get('/games')
def games__get__list():
    """Returns a list of all the games on the server"""
    return games_controller.games__get__list(request)


@bp.post('/games')
def games__post__create():
    """Creates a new game with the users in the request body as players"""
    return games_controller.games__post__create(request)


@bp.get('/games/{gameId}')
def some_game__get__info():
    """Returns all the data about the game with the given ID if such a game exists"""
    return games_controller.some_game__get__info(request)


@bp.put('/games/{gameId}')
def some_game__put__status():
    """Change the active/not active status of the game with the given ID (if one such exists)"""
    return games_controller.some_game__put__status(request)


@bp.post('/games/{gameId}/moves')
def some_game__post__move():
    """Perform another move in the game with the given ID by adding a move to the list of moves for this game"""
    return games_controller.some_game__post__move(request)

