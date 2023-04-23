from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.persistence.persistence_utils import find_all_users, find_user, persist_user
from flask import current_app


def users__get__list(request):
    users = find_all_users()
    schema = UserSchema()
    return [schema.dump(u) for u in users]


def users__post__create(request):
    body = request.get_json()
    user = User(username=body, rank=0)

    persist_user(user)

    return UserSchema().dump(user)


def some_user__get__info(request, username):
    user = find_user(username)

    return UserSchema().dump(user)


def rank__post__change(request, username):
    return "rank__post__change"
