import sqlite3


def create_users_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS USERS (
        ID INTEGER PRIMARY KEY,
        USERNAME TEXT NOT NULL,
        EXPERIENCE_POINT REAL DEFAULT 0
    )''')


def create_houses_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HOUSES (
        ID INTEGER PRIMARY KEY,
        HOUSE_NAME TEXT NOT NULL,
        HOUSE_DESCRIPTION TEXT
    )''')


def create_questions_table(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS QUESTIONS (
        ID INTEGER PRIMARY KEY,
        OPTION_A TEXT NOT NULL,
        OPTION_B TEXT NOT NULL,
        OPTION_C TEXT NOT NULL,
        OPTION_D TEXT NOT NULL,
        CORRECT_OPTION TEXT NOT NULL
    )''')


def insert_users_data(cursor):
    user_data_insert = [
        (1, 'user1', 0),
        (2, 'user2', 0),
        (3, 'user3', 0),
    ]
    cursor.executemany("INSERT INTO USERS (ID, USERNAME, EXPERIENCE_POINT) VALUES (?, ?, ?)", user_data_insert)


def fetch_users_data(cursor):
    cursor.execute("SELECT ID, USERNAME, EXPERIENCE_POINT FROM USERS")
    user_data_result = cursor.fetchall()
    return user_data_result


def main():
    with sqlite3.connect('../../AIGame.db') as connection:
        cursor = connection.cursor()

        try:
            create_users_table(cursor)
            create_houses_table(cursor)
            create_questions_table(cursor)
            # insert_users_data(cursor)
            user_data_result = fetch_users_data(cursor)
            print(user_data_result)
        except sqlite3.Error as e:
            print("An error occurred:", e)
