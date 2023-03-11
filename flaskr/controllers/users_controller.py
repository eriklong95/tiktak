def users__get__list(request):
    return "users__get__list"


def users__post__create(request):
    body = request.get_json()
    username = body["username"]
    return f"users__post__create: {username}"


def some_user__get__info(request):
    return "some_user__get__info"
