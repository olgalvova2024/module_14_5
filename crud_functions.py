import sqlite3

def initiate_db():
    connection = sqlite3.connect('database_14_4.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_id ON Products(id)')

    # for i in range(1,5):
    #     cursor.execute('INSERT INTO Products(title, description, price) VALUES(?,?,?)',
    #     (f'Продукт{i}', f'Описание{i}', f'{i*100}'))

    connection.commit()
    # connection.close()

    connection = sqlite3.connect('database_14_5.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        id INT PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INT NOT NULL,
        balance INT NOT NULL
        )
        ''')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('database_14_4.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    connection.commit()
    connection.close()
    return all_products

def is_included(username):
    connection = sqlite3.connect('database_14_5.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE username = ?;', (username,))
    user = cursor.fetchone()
    connection.commit()
    connection.close()
    return bool(user)

def add_user(username, email, age):
    connection = sqlite3.connect('database_14_5.db')
    cursor = connection.cursor()
    if not is_included(username):
        cursor.execute("INSERT INTO Users (username, email, age, balance) "
                       "VALUES (?, ?, ?, ?)", (username, email, age, "1000"))
    connection.commit()
    connection.close()

