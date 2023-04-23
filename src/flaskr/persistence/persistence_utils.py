from src.flaskr.persistence.repositories.user_repository import UserRepository


def find_all_users():
    repo = UserRepository()
    return repo.select_all_users()


def find_user(username):
    repo = UserRepository()
    return repo.select_user(username)


def persist_user(user):
    repo = UserRepository()
    repo.insert(user)
    repo.commit()


def update_user(user):
    repo = UserRepository()
    repo.update(user)
    repo.commit()