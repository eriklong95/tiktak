from marshmallow import Schema, fields


class GameInput(object):
    def __init__(self, challenger, opponent):
        self.challenger = challenger
        self.opponent = opponent

    def __repr__(self) -> str:
        return f"GameInput(challenger={self.challenger}, opponent={self.opponent})"
    

class GameInputSchema(Schema):
    challenger = fields.Str(required=True)
    opponent = fields.Str(required=True)
    