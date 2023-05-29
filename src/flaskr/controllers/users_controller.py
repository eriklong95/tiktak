from flask import make_response
from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.persistence.repositories.user_repository_api import UserRepositoryApi


USER_SCHEMA = UserSchema()


def users__get__list(request):
    repo = UserRepositoryApi()
    users = repo.select_all_users()
    return make_response([USER_SCHEMA.dump(u) for u in users], 200)


def users__post__create(request):
    # TODO: implement

    return make_response('Not yet implemented', 500)


def some_user__get__info(request, username):
    # TODO: implement

    return make_response('Not yet implemented', 500)
