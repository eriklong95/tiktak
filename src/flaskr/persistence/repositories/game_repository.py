from src.flaskr.models.game_model import Game


class GameRepository:
    def __init__(self, db_connection_supplier):
        self.insertions = []
        self.updates = []
        self.connection_supplier = db_connection_supplier

    def select_all_games(self):
        games_from_db = self.__select_all_games_from_db__()
        all_games_in_repo = games_from_db + self.insertions
        updated_games = self.__run_updates__(games=all_games_in_repo)
        return updated_games

    def __select_all_games_from_db__(self):
        connection = self.connection_supplier.get()
        cursor = connection.cursor()
        game_rows = cursor.execute('SELECT * FROM game').fetchall()
        connection.close()
        return [self.__row_to_object__(r) for r in game_rows]

    def __row_to_object__(self, game_row):
        return Game(id=game_row[0], player_a=game_row[1], player_b=game_row[2], moves=[])

    def __run_updates__(self, games):
        return [self.__run_update__(g) for g in games]

    def __run_update__(self, game):
        updated_game = game

        for update in self.updates:
            if update.id == game.id:
                updated_game = update

        return updated_game

    def select_game(self, game_id):
        game_in_insertions = self.__find_game_in_insertions__(game_id=game_id)
        if game_in_insertions is not None:
            updated_game = self.__run_update__(game=game_in_insertions)
            return updated_game

        game_in_db = self.__select_game_from_db__(game_id=game_id)
        if game_in_db is not None:
            updated_game = self.__run_update__(game=game_in_db)
            return updated_game

        return None

    def __find_game_in_insertions__(self, game_id):
        insertions = list(filter(lambda g: g.id == game_id, self.insertions))

        if len(insertions) > 0:
            return insertions[0]
        else:
            return None

    def __select_game_from_db__(self, game_id):
        connection = self.connection_supplier.get()
        cursor = connection.cursor()
        game_row = cursor.execute(
            'SELECT * FROM game WHERE id = ?', (game_id, )).fetchone()
        connection.close()

        if game_row is None:
            return None
        else:
            return self.__row_to_object__(game_row)

    def insert(self, game):
        if self.select_game(game_id=game.id) is not None:
            raise RuntimeError('Game already inserted: ' + game.id)

        self.insertions.append(game)

    def update(self, game):
        if self.select_game(game_id=game.id) is None:
            raise RuntimeError('Unknown game: ' + game.id)

        self.updates.append(game)

    def commit(self):
        connection = self.connection_supplier.get()
        self.__execute_insertions__(connection=connection)
        self.__execute_updates__(connection=connection)
        connection.close()

    def __execute_insertions__(self, connection):
        cursor = connection.cursor()
        game_rows = [self.__object_to_row__(g) for g in self.insertions]
        cursor.executemany('INSERT INTO game VALUES(?, ?, ?)', game_rows)
        connection.commit()
        self.insertions.clear()

    def __object_to_row__(self, game_object):
        return (game_object.id, game_object.player_a, game_object.player_b, )

    def __execute_updates__(self, connection):
        cursor = connection.cursor()

        for game in self.updates:
            cursor.execute('UPDATE game SET player_a = ?, player_b = ? WHERE id = ?',
                           (game.player_a, game.player_b, game.id, ))

        connection.commit()
        self.updates.clear()
