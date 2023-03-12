import unittest

from flaskr.models.user_model import User, UserSchema
from flaskr.models.game_model import GameInput, GameInputSchema


class TestUserSerialization(unittest.TestCase):
    def test_serialize_user(self):
        my_user = User(username="test")
        schema = UserSchema()
        json = schema.dump(my_user)
        self.assertEqual(json["username"], "test")


class TestGameInputSerialization(unittest.TestCase):
    def test_serialize_game_input(self):
        my_game_input = GameInput(challenger="test", opponent="test2")
        schema = GameInputSchema()
        json = schema.dump(my_game_input)
        self.assertEqual(json["challenger"], "test")
        self.assertEqual(json["opponent"], "test2")
