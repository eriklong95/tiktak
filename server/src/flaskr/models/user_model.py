from marshmallow import Schema, fields, post_load


class User(object):
    def __init__(self, username, rank):
        self.username = username
        self.rank = rank


    def __repr__(self):
        return f"User(username={self.username}, rank={self.rank})"
    

class UserSchema(Schema):
    username = fields.Str(required=True)
    rank = fields.Int(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)
    

