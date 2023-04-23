import sqlite3
from flask import current_app
from src.flaskr.models.user_model import User
from src.flaskr.persistence.repositories.user_cache import UserCache


DATABASE = 'database.db'


def create_user_row(user_object):
    return (user_object.username, user_object.rank)


def user_row_to_object(user_row):
    return User(username=user_row[0], rank=user_row[1])


class UserRepository:
    def __init__(self):
        self.users_to_insert = []
        self.users_to_update = []
        self.cache = UserCache()

    def select_all_users(self):
        if self.cache.valid:
            current_app.logger.info('Cache hit!')
            return self.cache.select_all_users()
        else:
            self.cache.invalidate()
            con = sqlite3.connect(DATABASE)
            cur = con.cursor()
            user_rows = cur.execute('SELECT * FROM user').fetchall()
            return [user_row_to_object(r) for r in user_rows]
        
    def select_user(self, username):
        if self.cache.valid:
            current_app.logger.info('Cache hit!')
            return self.cache.select_user(username)

    def insert(self, user):
        if self.select_user(user.username) is not None:
            raise RuntimeError('User already exists')
        elif len(list(filter(lambda u: u.username == user.username, self.users_to_insert))) > 0:
            raise RuntimeError('User already inserted')

        self.users_to_insert.append(user)

    def update(self, user):
        self.users_to_update.append(user)

    def commit(self):
        self.cache.invalidate()

        connection = sqlite3.connect(database=DATABASE)

        self.__execute_insertions(connection)
        self.__execute_updates(connection)

    def __execute_insertions(self, connection):
        cursor = connection.cursor()
        user_rows = [create_user_row(u) for u in self.users_to_insert]
        cursor.executemany('INSERT INTO user VALUES(?, ?)', user_rows)
        connection.commit()

    def __execute_updates(self, connection):
        pass
