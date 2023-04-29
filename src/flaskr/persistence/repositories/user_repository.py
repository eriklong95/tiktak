from src.flaskr.models.user_model import User


def create_user_row(user_object):
    return (user_object.username, user_object.rank)


def user_row_to_object(user_row):
    return User(username=user_row[0], rank=user_row[1])


class UserRepository:
    def __init__(self, database_connection_supplier):
        self.users_to_insert = []
        self.user_updates = []
        self.connection_supplier = database_connection_supplier

    def select_all_users(self):
        users_from_db = self.__select_all_users_from_db()
        all_users_in_repo = users_from_db + self.users_to_insert
        updated_users = self.__run_updates(users=all_users_in_repo)
        return updated_users

    def __select_all_users_from_db(self):
        connection = self.connection_supplier.get()
        cursor = connection.cursor()
        user_rows = cursor.execute('SELECT * FROM user').fetchall()
        connection.close()
        return [user_row_to_object(r) for r in user_rows]

    def __run_updates(self, users):
        list = []

        for user in users:
            updated_user = self.__run_update(user)
            list.append(updated_user)

        return list

    def __run_update(self, user):
        updated_user = user

        for update in self.user_updates:
            if update.username == user.username:
                updated_user = update

        return updated_user

    def select_user(self, username):
        user_from_db = self.__select_user_from_db(username=username)
        user_in_insertions = self.__find_user_in_insertions(username=username)

        if user_from_db is not None:
            updated_user = self.__run_update(user=user_from_db)
            return updated_user
        elif user_in_insertions is not None:
            updated_user = self.__run_update(user=user_in_insertions)
        else:
            return None

    def __select_user_from_db(self, username):
        connection = self.connection_supplier.get()
        cursor = connection.cursor()
        user_row = cursor.execute(
            'SELECT * FROM user WHERE username = ?', (username, )).fetchone()
        connection.close()

        if user_row is None:
            return None
        else:
            return user_row_to_object(user_row)

    def __find_user_in_insertions(self, username):
        insertions = list(filter(lambda u: u.username ==
                          username, self.users_to_insert))

        if len(insertions) > 0:
            return insertions[0]
        else:
            return None

    def insert(self, user):
        if self.select_user(user.username) is not None:
            raise RuntimeError('User already exists: ' + user.username)
        elif len(list(filter(lambda u: u.username == user.username, self.users_to_insert))) > 0:
            raise RuntimeError('User already inserted: ' + user.username)

        self.users_to_insert.append(user)

    def update(self, user):
        user_from_db = self.__select_user_from_db(username=user.username)
        user_in_insertions = self.__find_user_in_insertions(username=user.username)
        if user_from_db is None and user_in_insertions is None:
            raise RuntimeError('Unknown user: ' + user.username)

        self.user_updates.append(user)

    def commit(self):
        connection = self.connection_supplier.get()

        self.__execute_insertions(connection)
        self.__execute_updates(connection)
        connection.close()

    def __execute_insertions(self, connection):
        cursor = connection.cursor()
        user_rows = [create_user_row(u) for u in self.users_to_insert]
        cursor.executemany('INSERT INTO user VALUES(?, ?)', user_rows)
        connection.commit()
        self.users_to_insert.clear()

    def __execute_updates(self, connection):
        cursor = connection.cursor()

        for user in self.user_updates:
            cursor.execute(
                'UPDATE user SET rank = ? WHERE username = ?', (user.rank, user.username, ))

        connection.commit()
        self.user_updates.clear()
