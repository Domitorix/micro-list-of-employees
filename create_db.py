import sqlite3

connection = sqlite3.connect('database.db')

coursor = connection.cursor()
coursor.execute('''
    CREATE TABLE IF NOT EXISTS worker
    ''')

connection.close()