from src.flaskr.persistence.repositories.user_repository import UserRepository


def find_all_users():
    repo = UserRepository()
    return repo.select_all_users()


def persist_user(user):
    repo = UserRepository()
    repo.insert(user)
    repo.commit()
    return