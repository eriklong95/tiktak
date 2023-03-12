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
    return {
        "username": username
    }


def some_user__get__info(request):
    return "some_user__get__info"
