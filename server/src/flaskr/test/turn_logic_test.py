import unittest

from src.flaskr.controllers.turn_logic import derive_turn
from src.flaskr.models.game_model import Game, Move

class TestTurnDerivation(unittest.TestCase):
    def test_a_has_turn_in_fresh_game(self):
        game = Game('id', 'user', 'other-user', [])
        turn = derive_turn(game)
        self.assertEqual(turn, 'A')

    def test_b_has_second_turn(self):
        game = Game('id', 'user', 'other-user', [Move(x=0, y=0, occupier='A')])
        turn = derive_turn(game)
        self.assertEqual(turn, 'B')

    def test_players_have_made_same_number_of_moves(self):
        game = Game('id', 'user', 'other-user', [Move(x=0, y=0, occupier='A'), Move(x=0, y=1, occupier='B')])
        turn = derive_turn(game)
        self.assertEqual(turn, 'A')
