from src.flaskr.models.game_model import Game, Move


class GameRepository:
    def __init__(self, db_connection_supplier):
        self.game_insertions = []
        self.move_rows_to_insert = []
        self.connection_supplier = db_connection_supplier

    def select_all_games(self):
        games_from_db = self.__select_all_games_from_db__()
        games_in_insertions = self.__find_all_games_in_insertions__()
        return games_from_db + games_in_insertions

    def __select_all_games_from_db__(self):
        connection = self.connection_supplier.get()
        cursor = connection.cursor()
        game_rows = cursor.execute('SELECT * FROM game').fetchall()

        result = []
        for game_row in game_rows:
            move_rows = cursor.execute(
                'SELECT * FROM move WHERE game_id = ?', (game_row[0], ))

            for m in self.move_rows_to_insert:
                if m[3] == game_row[0]:
                    move_rows.append(m)

            result.append(self.__game_row_to_object__(game_row, move_rows))
        connection.close()

        return result

    def __game_row_to_object__(self, game_row, move_rows):
        move_objects = [self.__move_row_to_object__(m) for m in move_rows]
        return Game(id=game_row[0], player_a=game_row[1], player_b=game_row[2], moves=move_objects)

    def __move_row_to_object__(self, move_row):
        return Move(x=move_row[0], y=move_row[1], occupier=move_row[2])

    def __find_all_games_in_insertions__(self):
        result = []

        for game in self.game_insertions:
            associated_move_rows = list(
                filter(lambda m: m[3] == game.id, self.move_rows_to_insert))
            move_objects = [self.__move_row_to_object__(
                r) for r in associated_move_rows]
            game.moves.extend(move_objects)
            result.append(game)

        return result

    def select_game(self, game_id):
        game_in_insertions = self.__find_game_in_insertions__(game_id=game_id)
        if game_in_insertions is not None:
            return game_in_insertions

        return self.__select_game_from_db__(game_id=game_id)

    def __find_game_in_insertions__(self, game_id):
        insertions = list(
            filter(lambda g: g.id == game_id, self.game_insertions))

        if len(insertions) > 0:
            game = insertions[0]
            move_rows_in_insertions = list(
                filter(lambda m: m[3] == game_id, self.move_rows_to_insert))
            game.moves.extend(move_rows_in_insertions)
            return game
        else:
            return None

    def __select_game_from_db__(self, game_id):
        connection = self.connection_supplier.get()
        cursor = connection.cursor()
        game_row = cursor.execute(
            'SELECT * FROM game WHERE id = ?', (game_id, )).fetchone()
        move_rows_in_db = cursor.execute(
            'SELECT * FROM move WHERE game_id = ?', (game_id, )).fetchall()
        connection.close()

        move_rows_in_insertions = list(
            filter(lambda m: m[3] == game_id, self.move_rows_to_insert))

        if game_row is None:
            return None
        elif move_rows_in_db is None:
            return self.__game_row_to_object__(game_row=game_row, move_rows=move_rows_in_insertions)
        else:
            return self.__game_row_to_object__(game_row, move_rows_in_db + move_rows_in_insertions)

    def insert(self, game):
        if self.select_game(game_id=game.id) is not None:
            raise RuntimeError('Game already inserted: ' + game.id)

        self.game_insertions.append(game)

    def insert_move(self, move, game_id):
        if self.select_game(game_id) is None:
            raise RuntimeError('No game with this ID: ' + game_id)
        
        self.move_rows_to_insert.append(
            (move.x, move.y, move.occupier, game_id, ))

    def commit(self):
        connection = self.connection_supplier.get()
        self.__execute_game_insertions__(connection=connection)
        self.__execute_move_insertions__(connection=connection)
        connection.close()

    def __execute_game_insertions__(self, connection):
        cursor = connection.cursor()

        for game in self.game_insertions:
            cursor.execute('INSERT INTO game VALUES(?, ?, ?)',
                           self.__game_object_to_row__(game_object=game))
            move_rows = [self.__move_object_to_row__(
                m, game_id=game.id) for m in game.moves]
            cursor.executemany(
                'INSERT INTO move VALUES(?, ?, ?, ?)', move_rows)

        connection.commit()
        self.game_insertions.clear()

    def __execute_move_insertions__(self, connection):
        cursor = connection.cursor()
        cursor.executemany(
            'INSERT INTO move VALUES(?, ?, ?, ?)', self.move_rows_to_insert)
        connection.commit()
        self.move_rows_to_insert.clear()

    def __game_object_to_row__(self, game_object):
        return (game_object.id, game_object.player_a, game_object.player_b, )

    def __move_object_to_row__(self, move, game_id):
        return (move.x, move.y, move.occupier, game_id, )
