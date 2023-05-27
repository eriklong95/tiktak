import unittest

from src.flaskr.models.user_model import UserSchema
from src.flaskr.models.game_model import GameInputSchema, GameSchema, MoveSchema


class TestUserDeserialization(unittest.TestCase):
    def test_deserialize_user(self):
        json = {"username": "test", "rank": 0}
        schema = UserSchema()
        user = schema.load(json)
        self.assertEqual(user.username, "test")


class TestGameInputDeserialization(unittest.TestCase):
    def test_deserialize_game_input(self):
        json = {"challenger": "test", "opponent": "test2"}
        schema = GameInputSchema()
        game_input = schema.load(json)
        self.assertEqual(game_input.challenger, "test")
        self.assertEqual(game_input.opponent, "test2")


class TestGameDeserialization(unittest.TestCase):
    def test_deserialize_game(self):
        json = {
            "id": "test-id",
            "playerA": "test-player-a",
            "playerB": "test-player-b",
            "moves": [{"x": 0, "y": 0, "occupier": "A"}, {"x": 1, "y": 1, "occupier": "B"}]
        }
        schema = GameSchema()
        game = schema.load(json)
        self.assertEqual(game.id, "test-id")
        self.assertEqual(game.player_a, "test-player-a")
        self.assertEqual(game.player_b, "test-player-b")
        self.assertEqual(game.moves[0].x, 0)
        self.assertEqual(game.moves[0].y, 0)
        self.assertEqual(game.moves[0].occupier, "A")
        self.assertEqual(game.moves[1].x, 1)
        self.assertEqual(game.moves[1].y, 1)
        self.assertEqual(game.moves[1].occupier, "B")


class TestMoveDeserialization(unittest.TestCase):
    def test_deserialize_move(self):
        json = {"x": 0, "y": 0, "occupier": "A"}
        schema = MoveSchema()
        move = schema.load(json)
        self.assertEqual(move.x, 0)
        self.assertEqual(move.y, 0)
        self.assertEqual(move.occupier, "A")
