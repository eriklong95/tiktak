from src.flaskr.persistence.repositories.user_repository import UserRepository
from src.flaskr.persistence.db_connection.db_connection_supplier import DatabaseConnectionSupplier


class UserRepositoryApi:
    def __init__(self):
        self.impl = UserRepository(DatabaseConnectionSupplier())

    def select_all_users(self):
        '''Returns all users in the repository.'''
        return self.impl.select_all_users()

    def select_user(self, username):
        '''
            If a user with this username can be found in 
            the repository, return this user. Otherwise,
            return None.

            Parameters (other than self):
            username -- username of the user to be selected, as a string
        '''
        return self.impl.select_user(username=username)

    def insert(self, user):
        '''
            Insert this user in the repository.

            Parameters (other than self):
            user -- the user to be inserted, as a User object
        '''
        self.impl.insert(user=user)
        return self

    def update(self, user):
        '''
            Update this user in the repository.

            Parameters (other than self):
            user -- a User object representing the desired state of the
                user with the username user.username
        '''
        self.impl.update(user=user)
        return self

    def commit(self):
        '''Save the changes to the repository in the database.'''
        self.impl.commit()
