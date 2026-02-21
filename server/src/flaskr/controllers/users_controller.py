from flask import make_response
from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.persistence.repositories.user_repository_api import UserRepositoryApi


USER_SCHEMA = UserSchema()


def users__get__list(request):
    repo = UserRepositoryApi()
    users = repo.select_all_users()
    return make_response([USER_SCHEMA.dump(u) for u in users], 200)


def users__post__create(request):
    username = request.get_json()
    repo = UserRepositoryApi()

    if repo.select_user(username) is not None:
        return make_response('A user with this username already exists', 403)

    user = User(username=username, rank=0)

    repo.insert(user).commit()

    return make_response(USER_SCHEMA.dump(user), 201)


def some_user__get__info(request, username):
    repo = UserRepositoryApi()
    user = repo.select_user(username)

    if user is None:
        return make_response('No such user exists', 404)

    return make_response(USER_SCHEMA.dump(user), 200)


def rank__post__change(request, username):
    repo = UserRepositoryApi()
    user = repo.select_user(username)

    if user is None:
        return make_response('No such user exists', 404)

    body = request.get_json()
    updated_user = User(username=username, rank=user.rank + body)
    repo.update(updated_user).commit()

    return make_response(USER_SCHEMA.dump(updated_user), 200)
