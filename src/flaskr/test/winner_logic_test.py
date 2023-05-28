import unittest

from src.flaskr.controllers.winner_logic import find_winner
from src.flaskr.models.game_model import Game, Move

class TestFindWinner(unittest.TestCase):
    def test_fresh_game_is_undecided(self):
        game = Game('id', 'user', 'other-user', [])
        winner = find_winner(game)
        self.assertEqual(winner, 'undecided')

    def test_vertical_win(self):
        game = Game('id', 'user', 'other-user', [
            Move(x=1, y=0, occupier='A'),
            Move(x=0, y=1, occupier='B'),
            Move(x=1, y=1, occupier='A'),
            Move(x=2, y=1, occupier='B'),
            Move(x=1, y=2, occupier='A')
        ])
        winner = find_winner(game)
        self.assertEqual(winner, 'A')

    def test_horizontal_win(self):
        game = Game('id', 'user', 'other-user', [
            Move(x=0, y=2, occupier='A'),
            Move(x=0, y=0, occupier='B'),
            Move(x=1, y=1, occupier='A'),
            Move(x=1, y=0, occupier='B'),
            Move(x=2, y=2, occupier='A'),
            Move(x=2, y=0, occupier='B')
        ])
        winner = find_winner(game)
        self.assertEqual(winner, 'B')

    def test_diagonal_win(self):
        game = Game('id', 'user', 'other-user', [
            Move(x=0, y=2, occupier='A'),
            Move(x=0, y=0, occupier='B'),
            Move(x=1, y=1, occupier='A'),
            Move(x=2, y=2, occupier='B'),
            Move(x=2, y=0, occupier='A')
        ])
        winner = find_winner(game)
        self.assertEqual(winner, 'A')

    def test_game_in_deadlock(self):
        game = Game('id', 'user', 'other-user', [
            Move(x=0, y=2, occupier='A'),
            Move(x=0, y=0, occupier='B'),
            Move(x=1, y=0, occupier='A'),
            Move(x=2, y=0, occupier='B'),
            Move(x=0, y=1, occupier='A'),
            Move(x=1, y=2, occupier='B'),
            Move(x=1, y=1, occupier='A'),
            Move(x=2, y=1, occupier='B'),
            Move(x=2, y=2, occupier='A')
        ])
        winner = find_winner(game)
        self.assertEqual(winner, 'undecided')
