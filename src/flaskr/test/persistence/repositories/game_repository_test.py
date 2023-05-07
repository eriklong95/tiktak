import unittest
from src.flaskr.models.game_model import Game, Move
from src.flaskr.persistence.repositories.game_repository import GameRepository

from src.flaskr.test.persistence.mock_db_connection_supplier import MockDatabaseConnectionSupplier


class TestGameInsertion(unittest.TestCase):
    def test_insert_game(self):
        sut = GameRepository(MockDatabaseConnectionSupplier())

        game = Game('7agd87asf7d8f', 'demouser', 'stranger', [])
        sut.insert(game=game)
        result = sut.select_game(game_id=game.id)

        self.assertIsNotNone(result)
