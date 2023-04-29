import sqlite3


DATABASE = 'database.db'

class DatabaseConnectionSupplier:
    def get(self):
        return sqlite3.connect(DATABASE)
