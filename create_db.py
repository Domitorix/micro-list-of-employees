import sqlite3

connection = sqlite3.connect('database.db')

coursor = connection.cursor()
coursor.execute('''
    CREATE TABLE IF NOT EXISTS Worker (
    id Integer PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    phone INTEGER,
    email TEXT   
    )
    ''')


def add_user(f_name, l_name, a_phone, a_email):
    coursor.execute('INSERT INTO Worker (first_name, last_name, phone, email) VALUES (?, ?, ?, ?)', (f_name, l_name, a_phone, a_email))
    connection.commit()
    
    

def update_user(fix_1, fix_2, fix_3):
    coursor.execute(f'UPDATE Worker SET {fix_1} = ? WHERE last_name = ?', (fix_2, fix_3))
    connection.commit()
    
def delete_user(del_1):
    coursor.execute('DELETE FROM Worker WHERE last_name = ?', (del_1,))
    connection.commit()
 
def all_workers():
    coursor.execute('SELECT * FROM Worker')
    workers = coursor.fetchall()
    
    for worker in workers:
        print(worker)

def exit():
    connection.close()
    
    


#connection.commit()
#connection.close()