import unittest
from src.flaskr.models.user_model import User

from src.flaskr.persistence.repositories.user_repository import UserRepository
from src.flaskr.test.persistence.mock_db_connection_supplier import MockDatabaseConnectionSupplier


class TestUserInsertion(unittest.TestCase):
    def test_insert_user(self):
        sut = UserRepository(MockDatabaseConnectionSupplier())

        user = User(username='demouser', rank=0)
        sut.insert(user)
        result = sut.select_user('demouser')

        self.assertIsNotNone(result)


class TestUserUpdate(unittest.TestCase):
    def test_update_user(self):
        sut = UserRepository(MockDatabaseConnectionSupplier())

        user = User(username='demouser', rank=0)
        sut.insert(user)
        user = User(username='demouser', rank=1)
        sut.update(user)
        result = sut.select_user('demouser')

        self.assertEqual(result.rank, 1)
