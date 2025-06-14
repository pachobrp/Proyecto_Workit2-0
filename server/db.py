import sqlite3

def get_connection():
    conn = sqlite3.connect('database.sqlite')
    conn.row_factory = sqlite3.Row  # Esto permite acceder a las columnas por nombre
    return conn
