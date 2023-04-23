class UserCache:
    def __init__(self):
        self.valid = False
        self.__users = []

    def invalidate(self):
        self.valid = False

    def cache(self, users):
        self.__users = users

    def select_all_users(self):
        if self.valid:
            return self.__users
        else:
            raise RuntimeError('Invalid cache')

    def select_user(self, username):
        if not self.valid:
            raise RuntimeError('Invalid cache')

        users_with_this_username = list(
            filter(lambda u: u.username == username, self.__users))

        if len(users_with_this_username) > 0:
            return users_with_this_username[0]
        else:
            return None
