import unittest

from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.models.game_model import GameInput, GameInputSchema


class TestUserDeserialization(unittest.TestCase):
    def test_deserialize_user(self):
        json = {"username": "test"}
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