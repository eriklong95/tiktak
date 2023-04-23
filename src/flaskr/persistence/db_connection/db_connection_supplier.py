import sqlite3


DATABASE = 'database.db'

def get():
    return sqlite3.connect(DATABASE)
