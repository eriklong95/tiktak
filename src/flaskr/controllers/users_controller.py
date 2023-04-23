from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.persistence.persistence_utils import find_all_users, find_user, persist_user, update_user


USER_SCHEMA = UserSchema()

def users__get__list(request):
    users = find_all_users()
    return [USER_SCHEMA.dump(u) for u in users]


def users__post__create(request):
    body = request.get_json()
    user = User(username=body, rank=0)

    persist_user(user)

    return USER_SCHEMA.dump(user)


def some_user__get__info(request, username):
    user = find_user(username)

    return USER_SCHEMA.dump(user)


def rank__post__change(request, username):
    user = find_user(username)

    body = request.get_json()

    updated_user = User(username=username, rank=user.rank + body)

    update_user(user=updated_user)

    return USER_SCHEMA.dump(updated_user)
