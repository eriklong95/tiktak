from marshmallow import Schema, fields, post_load


class GameInput(object):
    def __init__(self, challenger, opponent):
        self.challenger = challenger
        self.opponent = opponent

    def __repr__(self) -> str:
        return f"GameInput(challenger={self.challenger}, opponent={self.opponent})"
    

class GameInputSchema(Schema):
    challenger = fields.Str(required=True)
    opponent = fields.Str(required=True)

    @post_load
    def make_game_input(self, data, **kwargs):
        return GameInput(**data)
    

class Game(object):
    def __init__(self, id, challenger, opponent, state):
        self.id = id
        self.challenger = challenger
        self.opponent = opponent
        self.state = state

    def __repr__(self) -> str:
        return f"Game(id={self.id}, challenger={self.challenger}, opponent={self.opponent}, state={self.state})"
    

class GameSchema(Schema):
    id = fields.Str(required=True)
    challenger = fields.Str(required=True)
    opponent = fields.Str(required=True)
    state = fields.Nested("GameStateSchema", required=True)

    @post_load
    def make_game(self, data, **kwargs):
        return Game(**data)
    

class GameState(object):
    def __init__(self, turn, moves):
        self.turn = turn
        self.moves = moves


class GameStateSchema(Schema):
    turn = fields.Str(required=True)
    moves = fields.List(fields.Nested("MoveSchema"), required=True)

    @post_load
    def make_game_state(self, data, **kwargs):
        return GameState(**data)


class Move(object):
    def __init__(self, x, y, occupier):
        self.x = x
        self.y = y
        self.occupier = occupier

    def __repr__(self) -> str:
        return f"Move(x={self.x}, y={self.y}, occupier={self.occupier})"


class MoveSchema(Schema):
    x = fields.Int(required=True)
    y = fields.Int(required=True)
    occupier = fields.Str(required=True)

    @post_load
    def make_move(self, data, **kwargs):
        return Move(**data)
    