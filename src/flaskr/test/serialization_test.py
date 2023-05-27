import unittest

from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.models.game_model import Game, GameInput, GameInputSchema, GameSchema, Move, MoveSchema


class TestUserSerialization(unittest.TestCase):
    def test_serialize_user(self):
        my_user = User(username="test", rank=0)
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


class TestGameSerialization(unittest.TestCase):
    def test_serialize_game(self):
        my_game = Game(id="test", player_a="test", player_b="test2", moves=[Move(x=0, y=0, occupier="A"), Move(x=1, y=1, occupier="B")])
        schema = GameSchema()
        json = schema.dump(my_game)
        self.assertEqual(json["id"], "test")
        self.assertEqual(json["playerA"], "test")
        self.assertEqual(json["playerB"], "test2")
        self.assertEqual(json["moves"][0]["x"], 0)
        self.assertEqual(json["moves"][0]["y"], 0)
        self.assertEqual(json["moves"][0]["occupier"], "A")
        self.assertEqual(json["moves"][1]["x"], 1)
        self.assertEqual(json["moves"][1]["y"], 1)
        self.assertEqual(json["moves"][1]["occupier"], "B")


class TestMoveSerialization(unittest.TestCase):
    def test_serialize_move(self):
        my_move = Move(x=0, y=0, occupier="test")
        schema = MoveSchema()
        json = schema.dump(my_move)
        self.assertEqual(json["x"], 0)
        self.assertEqual(json["y"], 0)
        self.assertEqual(json["occupier"], "test")