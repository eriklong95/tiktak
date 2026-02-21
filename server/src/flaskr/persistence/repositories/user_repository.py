from src.flaskr.models.user_model import User


class UserRepository:
    def __init__(self, database_connection_supplier):
        self.insertions = []
        self.updates = []
        self.connection_supplier = database_connection_supplier

    def select_all_users(self):
        users_from_db = self.__select_all_users_from_db__()
        all_users_in_repo = users_from_db + self.insertions
        updated_users = self.__run_updates__(users=all_users_in_repo)
        return updated_users

    def __select_all_users_from_db__(self):
        connection = self.connection_supplier.get()
        cursor = connection.cursor()
        user_rows = cursor.execute('SELECT * FROM user').fetchall()
        connection.close()
        return [self.__row_to_object__(r) for r in user_rows]

    def __row_to_object__(self, user_row):
        return User(username=user_row[0], rank=user_row[1])

    def __run_updates__(self, users):
        return [self.__run_update__(u) for u in users]

    def __run_update__(self, user):
        updated_user = user

        for update in self.updates:
            if update.username == user.username:
                updated_user = update

        return updated_user

    def select_user(self, username):
        user_in_insertions = self.__find_user_in_insertions__(
            username=username)
        if user_in_insertions is not None:
            updated_user = self.__run_update__(user=user_in_insertions)
            return updated_user

        user_from_db = self.__select_user_from_db__(username=username)
        if user_from_db is not None:
            updated_user = self.__run_update__(user=user_from_db)
            return updated_user

        return None

    def __find_user_in_insertions__(self, username):
        insertions = list(filter(lambda u: u.username ==
                          username, self.insertions))

        if len(insertions) > 0:
            return insertions[0]
        else:
            return None

    def __select_user_from_db__(self, username):
        connection = self.connection_supplier.get()
        cursor = connection.cursor()
        user_row = cursor.execute(
            'SELECT * FROM user WHERE username = ?', (username, )).fetchone()
        connection.close()

        if user_row is None:
            return None
        else:
            return self.__row_to_object__(user_row)

    def insert(self, user):
        if self.select_user(user.username) is not None:
            raise RuntimeError('User already inserted: ' + user.username)

        self.insertions.append(user)

    def update(self, user):
        if self.select_user(username=user.username) is None:
            raise RuntimeError('Unknown user: ' + user.username)

        self.updates.append(user)

    def commit(self):
        connection = self.connection_supplier.get()

        self.__execute_insertions__(connection)
        self.__execute_updates__(connection)
        connection.close()

    def __execute_insertions__(self, connection):
        cursor = connection.cursor()
        user_rows = [self.__object_to_row__(u) for u in self.insertions]
        cursor.executemany('INSERT INTO user VALUES(?, ?)', user_rows)
        connection.commit()
        self.insertions.clear()

    def __object_to_row__(self, user_object):
        return (user_object.username, user_object.rank)

    def __execute_updates__(self, connection):
        cursor = connection.cursor()

        for user in self.updates:
            cursor.execute(
                'UPDATE user SET rank = ? WHERE username = ?', (user.rank, user.username, ))

        connection.commit()
        self.updates.clear()
