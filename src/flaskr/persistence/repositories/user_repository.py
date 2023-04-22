import sqlite3


DATABASE = 'database.db'


def create_user_row(user_object):
    return (user_object.username, user_object.rank)


class UserRepository:
    def __init__(self):
        self.users_to_insert = []

    def insert(self, user):
        self.users_to_insert.append(user)

    def commit(self):
        connection = sqlite3.connect(database=DATABASE)
        cursor = connection.cursor()

        user_rows = [create_user_row(u) for u in self.users_to_insert]
        cursor.executemany('INSERT INTO user VALUES(?, ?)', user_rows)
        connection.commit()
