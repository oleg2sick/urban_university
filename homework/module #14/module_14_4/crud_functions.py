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

initiate_db()
db_filler()

