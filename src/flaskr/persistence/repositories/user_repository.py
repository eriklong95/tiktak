from src.flaskr.models.user_model import User
from src.flaskr.persistence.db_connection import db_connection_supplier


def create_user_row(user_object):
    return (user_object.username, user_object.rank)


def user_row_to_object(user_row):
    return User(username=user_row[0], rank=user_row[1])


class UserRepository:
    def __init__(self):
        self.users_to_insert = []
        self.users_to_update = []

    def select_all_users(self):
        users_from_db = self.__select_all_users_from_db()
        updated_users = self.__run_updates(users=users_from_db)
        return updated_users + self.users_to_insert

    def __select_all_users_from_db(self):
        con = db_connection_supplier.get()
        cur = con.cursor()
        user_rows = cur.execute('SELECT * FROM user').fetchall()
        return [user_row_to_object(r) for r in user_rows]

    def __run_updates(self, users):
        list = []

        for user in users:
            updated_user = self.__run_update(user)
            list.append(updated_user)

        return list

    def __select_user_from_db(self, username):
        con = db_connection_supplier.get()
        cur = con.cursor()
        user_row = cur.execute('SELECT * FROM user WHERE username = ?', (username, )).fetchone()

        if user_row is None:
            return None
        else:
            return user_row_to_object(user_row)

    def __run_update(self, user):
        my_list = list(filter(lambda u: u.username ==
                       user.username, self.users_to_update))
        if len(my_list) > 0:
            return list[0]
        else:
            return user

    def select_user(self, username):
        user_from_db = self.__select_user_from_db(username=username)
        user_in_insertions = self.__find_user_in_insertions(username=username)

        if user_from_db is not None:
            updated_user = self.__run_update(user=user_from_db)
            return updated_user
        else:
            return user_in_insertions

    def __find_user_in_insertions(self, username):
        insertions = list(filter(lambda u: u.username == username, self.users_to_insert))
        if len(insertions) > 0:
            return insertions[0]
        else:
            return None

    def insert(self, user):
        if self.select_user(user.username) is not None:
            raise RuntimeError('User already exists')
        elif len(list(filter(lambda u: u.username == user.username, self.users_to_insert))) > 0:
            raise RuntimeError('User already inserted')

        self.users_to_insert.append(user)

    def update(self, user):
        # TODO: what if user is updated multiple times
        self.users_to_update.append(user)

    def commit(self):
        connection = db_connection_supplier.get()

        self.__execute_insertions(connection)
        self.__execute_updates(connection)

    def __execute_insertions(self, connection):
        cursor = connection.cursor()
        user_rows = [create_user_row(u) for u in self.users_to_insert]
        cursor.executemany('INSERT INTO user VALUES(?, ?)', user_rows)
        connection.commit()
        self.users_to_insert.clear()

    def __execute_updates(self, connection):
        cursor = connection.cursor()

        for user in self.users_to_update:
            cursor.execute(
                'UPDATE user SET rank = ? WHERE username = ?', (user.rank, user.username, ))

        connection.commit()
        self.users_to_update.clear()
