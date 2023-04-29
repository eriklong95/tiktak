from src.flaskr.test.serialization_test import TestUserSerialization, TestGameInputSerialization, TestGameSerialization, TestMoveSerialization
from src.flaskr.test.deserialization_test import TestUserDeserialization, TestGameInputDeserialization, TestGameDeserialization, TestMoveDeserialization
from src.flaskr.persistence.db_connection.db_connection_supplier import DatabaseConnectionSupplier


connection = DatabaseConnectionSupplier().get()
cursor = connection.cursor()

all_tables_result = cursor.execute('SELECT name FROM sqlite_master')
tables = all_tables_result.fetchall()

user_table_exists = any(list(filter(lambda t: t[0] == 'user', tables)))
if not user_table_exists:
    cursor.execute('CREATE TABLE user(username, rank)')
    print('Created table \'user\'')

