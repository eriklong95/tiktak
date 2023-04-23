from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.persistence.repositories.user_repository import UserRepository


USER_SCHEMA = UserSchema()

def users__get__list(request):
    repo = UserRepository()
    users = repo.select_all_users()
    return [USER_SCHEMA.dump(u) for u in users]


def users__post__create(request):
    body = request.get_json()
    user = User(username=body, rank=0)

    repo = UserRepository()
    repo.insert(user).commit()

    return USER_SCHEMA.dump(user)


def some_user__get__info(request, username):
    repo = UserRepository()
    user = repo.select_user(username)

    return USER_SCHEMA.dump(user)


def rank__post__change(request, username):
    repo = UserRepository()
    user = repo.select_user(username)

    body = request.get_json()

    updated_user = User(username=username, rank=user.rank + body)

    repo = UserRepository()
    repo.update(updated_user).commit()

    return USER_SCHEMA.dump(updated_user)
