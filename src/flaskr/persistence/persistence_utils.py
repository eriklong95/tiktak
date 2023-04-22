from src.flaskr.persistence.repositories.user_repository import UserRepository


def find_all_users():
    return []


def persist_user(user):
    repo = UserRepository()
    repo.insert(user)
    repo.commit()
    return