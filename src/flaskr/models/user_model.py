from marshmallow import Schema, fields


class User(object):
    def __init__(self, username):
        self.username = username


    def __repr__(self):
        return f"User(username={self.username})"
    

class UserSchema(Schema):
    username = fields.Str(required=True)
    

