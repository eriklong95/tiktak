import unittest

from src.flaskr.models.user_model import User, UserSchema
from src.flaskr.models.game_model import GameInput, GameInputSchema, GameSchema, GameStateSchema, MoveSchema


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
            "challenger": "test-challenger", 
            "opponent": "test-opponent", 
            "state": {
                "turn": "A", 
                "moves": [{"x": 0, "y": 0, "occupier": "A"}, {"x": 1, "y": 1, "occupier": "B"}]
            }
        }
        schema = GameSchema()
        game = schema.load(json)
        self.assertEqual(game.id, "test-id")
        self.assertEqual(game.challenger, "test-challenger")
        self.assertEqual(game.opponent, "test-opponent")
        self.assertEqual(game.state.turn, "A")
        self.assertEqual(game.state.moves[0].x, 0)
        self.assertEqual(game.state.moves[0].y, 0)
        self.assertEqual(game.state.moves[0].occupier, "A")
        self.assertEqual(game.state.moves[1].x, 1)
        self.assertEqual(game.state.moves[1].y, 1)
        self.assertEqual(game.state.moves[1].occupier, "B")


class TestGameStateDeserialization(unittest.TestCase):
    def test_deserialize_game_state(self):
        json = {
            "turn": "A", 
            "moves": [{"x": 0, "y": 0, "occupier": "A"}, {"x": 1, "y": 1, "occupier": "B"}]
        }
        schema = GameStateSchema()
        game_state = schema.load(json)
        self.assertEqual(game_state.turn, "A")
        self.assertEqual(game_state.moves[0].x, 0)
        self.assertEqual(game_state.moves[0].y, 0)
        self.assertEqual(game_state.moves[0].occupier, "A")
        self.assertEqual(game_state.moves[1].x, 1)
        self.assertEqual(game_state.moves[1].y, 1)
        self.assertEqual(game_state.moves[1].occupier, "B")


class TestMoveDeserialization(unittest.TestCase):
    def test_deserialize_move(self):
        json = {"x": 0, "y": 0, "occupier": "A"}
        schema = MoveSchema()
        move = schema.load(json)
        self.assertEqual(move.x, 0)
        self.assertEqual(move.y, 0)
        self.assertEqual(move.occupier, "A")