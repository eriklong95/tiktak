from src.flaskr.models.user_model import User, UserSchema


def users__get__list(request):
    return 'request with query param "minRank" set to ' + request.args.get('minRank')


def users__post__create(request):
    body = request.get_json()
    print(body)
    user = User(username=body, rank=0)
    schema = UserSchema()
    return schema.dump(user)


def some_user__get__info(request, username):
    return "some_user__get__info"
