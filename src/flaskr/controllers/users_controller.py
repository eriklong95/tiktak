from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.persistence.persistence_utils import persist_user
from flask import current_app


def users__get__list(request):
    return []


def users__post__create(request):
    body = request.get_json()
    user = User(username=body, rank=0)

    persist_user(user)

    return UserSchema().dump(user)


def some_user__get__info(request, username):
    return "some_user__get__info"


def rank__post__change(request, username):
    return "rank__post__change"
