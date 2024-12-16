import sqlite3


def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGET NOT NULL
    )
    ''')

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT *'
                  'FROM Products'
                  )

    return cursor.fetchall()

    connection.commit()
    connection.close()


def db_filler():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'ручка', f'синяя', 100))
    cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'карандаш', f'мягкий', 200))
    cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'кисть', f'тонкая', 300))
    cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'фломастер', f'синий', 400))


    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'{username}', f'{email}', f'{age}', 1000))

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()

    check = cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    if check.fetchone() is None:
        return True
    else:
        return False

    connection.commit()
    connection.close()

initiate_db()
db_filler()

