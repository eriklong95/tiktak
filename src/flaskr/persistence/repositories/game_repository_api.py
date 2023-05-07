from src.flaskr.persistence.db_connection.db_connection_supplier import DatabaseConnectionSupplier
from src.flaskr.persistence.repositories.game_repository import GameRepository


class GameRepositoryApi:
    def __init__(self):
        self.impl = GameRepository(DatabaseConnectionSupplier())

    def select_all_games(self):
        '''Returns all games in the repository.'''
        return self.impl.select_all_games()

    def select_game(self, game_id):
        '''
            If a game with this id can be found in 
            the repository, return this game. Otherwise,
            return None.

            Parameters (other than self):
            gameId -- id of the game to be selected, as a string
        '''
        return self.impl.select_game(game_id=game_id)

    def insert(self, game):
        '''
            Insert this game in the repository.

            Parameters (other than self):
            game -- the game to be inserted, as a Game object
        '''
        self.impl.insert(game=game)
        return self

    def update(self, game):
        '''
            Update this user in the repository.

            Parameters (other than self):
            user -- a User object representing the desired state of the
                user with the username user.username
        '''
        self.impl.update(game=game)
        return self

    def commit(self):
        '''Save the changes to the repository in the database.'''
        self.impl.commit()
