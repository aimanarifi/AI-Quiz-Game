"""
AI Group Project Team 7 Spring22/23

Desc: Database connector
Created by: Zhongjie Huang
Modified by: Muhammad Kamaludin
Last modified: 11/4/2023
"""

import sqlite3

def create_users_table(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS USERS (
	"ID"	INTEGER NOT NULL,
	"USERNAME"	TEXT,
	"MONEY"	REAL NOT NULL DEFAULT 0,
	"EXPERIENCE"	REAL NOT NULL DEFAULT 0,
	"EXP_AI"	REAL NOT NULL DEFAULT 0,
	"EXP_BLOCKCHAIN"	REAL NOT NULL DEFAULT 0,
	"EXP_CLOUD"	REAL NOT NULL DEFAULT 0,
	"EXP_CYBERSECURITY"	REAL NOT NULL DEFAULT 0,
	"EXP_DATASCIENCE"	REAL NOT NULL DEFAULT 0,
	"EXP_IOT"	REAL NOT NULL DEFAULT 0,
	"HIGHSCORE_AI"	REAL NOT NULL DEFAULT 0,
	"HIGHSCORE_BLOCKCHAIN"	REAL NOT NULL DEFAULT 0,
	"HIGHSCORE_CLOUD"	REAL NOT NULL DEFAULT 0,
	"HIGHSCORE_CYBERSECURITY"	REAL NOT NULL DEFAULT 0,
	"HIGHSCORE_DATASCIENCE"	REAL NOT NULL DEFAULT 0,
	"HIGHSCORE_IOT"	REAL NOT NULL DEFAULT 0,
	PRIMARY KEY("ID" AUTOINCREMENT)
)''')


def create_houses_table(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS HOUSES (
        ID INTEGER PRIMARY KEY,
        HOUSE_NAME TEXT NOT NULL,
        HOUSE_DESCRIPTION TEXT
    )''')

def create_questions_table(cursor: sqlite3.Cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS QUESTIONS (
	"ID"	INTEGER,
	"QUESTION"	TEXT,
	"OPTION_A"	TEXT NOT NULL,
	"OPTION_B"	TEXT NOT NULL,
	"OPTION_C"	TEXT NOT NULL,
	"OPTION_D"	TEXT NOT NULL,
	"CORRECT_OPTION"	TEXT NOT NULL,
	"DIFFICULTY"	INTEGER NOT NULL,
	"HOUSE"	TEXT NOT NULL,
	PRIMARY KEY("ID")
)''')

def connect():
    try:
        conn = sqlite3.connect('AIGame.db')
        return conn
    except sqlite3.Error as e:
        print("Error occured in connection: ", e)

def disconnect(connection: sqlite3.Connection):
    if connection:
        connection.close()

def insert_user(username: str):
    #Only need name as other fields have default value
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO USERS USERNAME VALUES ?", username)
        conn.commit()
    except sqlite3.Error as e:
        print("Error while inserting user: ", e)
    finally:
        disconnect(conn)

def get_user():
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USERS")
        result = cursor.fetchone()
    except sqlite3.Error as e:
        print("Error while fetching user data: ", e)
    finally:
        disconnect(conn)

    return result

def update_user(player):
    """
    Update all columns according to the current values of instance variables of player object
    will be updated once player class is appropriately established

    this method can be use to save progress
    """
    return False

def insert_questions(csv_path:str):
    """
    this is a temporary function to automate insertion of all quizzes from a csv file
    """
    return False

def get_questions(house:str, difficulty:int=0 ):
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        query = f"SELECT QUESTION, OPTION_A, OPTION_B, OPTION_C, OPTION_D, CORRECT_OPTION, DIFFICULTY FROM QUESTIONS"
        query += f" AND DIFFICULTY = {difficulty}" if difficulty else ""
        cursor.execute(query)
        result = cursor.fetchall()
    except sqlite3.Error as error:
        print("Error occured when fetching questions: ", error)
    finally:
        disconnect(conn)
    return result

def init():
    """
    Initialize the database before the game start
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        try:
            create_users_table(cursor)
            create_houses_table(cursor)
            create_questions_table(cursor)
            connection.commit()
        except sqlite3.Error as e:
            print("An error occurred:", e)

init()