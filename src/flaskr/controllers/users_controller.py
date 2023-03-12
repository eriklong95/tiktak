from src.flaskr.models.user_model import User, UserSchema


def users__get__list(request):
    return [
        {
            "username": "user1",
        },
        {
            "username": "user2",
        },
    ]


def users__post__create(request):
    body = request.get_json()
    username = body["username"]
    user = User(username=username)
    schema = UserSchema()
    print("Created schema. Ready to dump.")
    return schema.dump(user)


def some_user__get__info(request):
    return "some_user__get__info"
