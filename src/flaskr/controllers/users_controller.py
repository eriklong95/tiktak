from flask import make_response
from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.persistence.repositories.user_repository_api import UserRepositoryApi


USER_SCHEMA = UserSchema()


def users__get__list(request):
    repo = UserRepositoryApi()
    users = repo.select_all_users()
    return make_response([u.username for u in users], 200)


def users__post__create(request):
    body = request.json
    new_user = User(body, 0)
    repo = UserRepositoryApi()

    existing_user = repo.select_user(new_user.username)
    
    if (existing_user != None):
        return make_response('A user with this username already exists', 403)

    repo.insert(new_user)
    repo.commit()
    return make_response(USER_SCHEMA.dump(new_user), 201)


def some_user__get__info(request, username):
    repo = UserRepositoryApi()
    user = repo.select_user(username)

    if (user == None):
        return make_response('No such user exists', 404)
    
    return make_response(USER_SCHEMA.dump(user), 200)

