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
    def __init__(self, id, player_a, player_b, moves):
        self.id = id
        self.player_a = player_a
        self.player_b = player_b
        self.moves = moves

    def __repr__(self) -> str:
        return f"Game(id={self.id}, player_a={self.player_a}, player_b={self.player_b}, moves={self.moves})"
    

class GameSchema(Schema):
    id = fields.Str(required=True, data_key='id')
    player_a = fields.Str(required=True, data_key='playerA')
    player_b = fields.Str(required=True, data_key='playerB')
    moves = fields.List(fields.Nested("MoveSchema"), required=True)

    @post_load
    def make_game(self, data, **kwargs):
        return Game(**data)
    

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
    