"""
Written by: Zhongjie Huang, Muhammad
Last modified: 27/04/2023
"""

import sqlite3
from project.production.general import quiz


def create_tables():
    """
    This function is used to create all tables needed for this project in the database.
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS USER (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            USERNAME TEXT,
            MONEY REAL NOT NULL DEFAULT 0,
            EXPERIENCE REAL NOT NULL DEFAULT 0,
            EXP_AI REAL NOT NULL DEFAULT 0,
            EXP_BLOCKCHAIN REAL NOT NULL DEFAULT 0,
            EXP_CLOUD REAL NOT NULL DEFAULT 0,
            EXP_CYBERSECURITY REAL NOT NULL DEFAULT 0,
            EXP_DATASCIENCE	REAL NOT NULL DEFAULT 0,
            EXP_IOT	REAL NOT NULL DEFAULT 0,
            HIGHSCORE_AI REAL NOT NULL DEFAULT 0,
            HIGHSCORE_BLOCKCHAIN REAL NOT NULL DEFAULT 0,
            HIGHSCORE_CLOUD	REAL NOT NULL DEFAULT 0,
            HIGHSCORE_CYBERSECURITY	REAL NOT NULL DEFAULT 0,
            HIGHSCORE_DATASCIENCE REAL NOT NULL DEFAULT 0,
            HIGHSCORE_IOT REAL NOT NULL DEFAULT 0
            )''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS QUESTIONS (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            QUESTION TEXT,
            OPTION_A TEXT NOT NULL,
            OPTION_B TEXT NOT NULL,
            OPTION_C TEXT NOT NULL,
            OPTION_D TEXT NOT NULL,
            CORRECT_OPTION TEXT NOT NULL,
            DIFFICULTY INTEGER NOT NULL,
            HOUSE TEXT NOT NULL
            )''')
            connection.commit()
        except sqlite3.Error as e:
            print("An error has occurred: ", e)
            connection.rollback()


def get_user():
    """
    This function is used to get the user's data, which will be returned in a tuple
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM USER")
            userData = cursor.fetchone()
        except sqlite3.Error as e:
            print("An error has occurred: ", e)
        return userData


def update_user(user):
    """
    This function is used to update user's data, each time when it is called, the user's data will be updated automatically if
    there is a change. e.g. part of save game progress.
    It takes a user instance as the parameter
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT money, experience, exp_ai, exp_blockchain, exp_cloud, "
                           "exp_cybersecurity, exp_datascience, exp_iot, highscore_ai, highscore_blockchain, "
                           "highscore_cloud, highscore_cybersecurity, highscore_datascience, highscore_iot FROM USER")
            userData = cursor.fetchone()
        except sqlite3.Error as e:
            print("An error has occurred: ", e)
        if user.money != userData[0] or user.experience != userData[1] or user.exp_ai != userData[
            2] or user.exp_blockchain != userData[3] \
                or user.exp_cloud != userData[4] or user.exp_cybersecurity != userData[5] or user.exp_datascience != \
                userData[6] or \
                user.exp_iot != userData[7] or user.highscore_ai != userData[8] or user.highscore_blockchain != \
                userData[9] or \
                user.highscore_cloud != userData[10] or user.highscore_cybersecurity != userData[
            11] or user.highscore_datascience != userData[12] \
                or user.highscore_iot != userData[13]:
            try:
                cursor.execute(
                    f"UPDATE USER SET money = {user.money}, experience = {user.experience}, exp_ai = {user.exp_ai}, "
                    f"exp_blockchain = {user.exp_blockchain}, exp_cloud = {user.exp_cloud}, "
                    f"exp_cybersecurity = {user.exp_cybersecurity}, exp_datascience = {user.exp_datascience}, exp_iot = {user.exp_iot}, "
                    f"highscore_ai = {user.highscore_ai}, highscore_blockchain = {user.highscore_blockchain}, "
                    f"highscore_cloud = {user.highscore_cloud}, highscore_cybersecurity = {user.highscore_cybersecurity}, "
                    f"highscore_datascience = {user.highscore_datascience}, highscore_iot = {user.highscore_iot}")
                connection.commit()
                print("User's data has been updated successfully")
            except sqlite3.Error as e:
                print("An error has occurred: ", e)
                connection.rollback()


def get_questions(difficulty: int, house: str):
    """
    This function is used to get all questions from the questions table.
    All questions corresponding to the difficulty condition will be returned in a tuple
    It takes a degree of difficulty and house name as parameters
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                f"SELECT QUESTION, OPTION_A, OPTION_B, OPTION_C, OPTION_D, CORRECT_OPTION FROM QUESTIONS WHERE DIFFICULTY = {difficulty} AND HOUSE = {house}")
            questions = cursor.fetchone()
        except sqlite3.Error as e:
            print("An error has occurred: ", e)
        for question in len(questions):
            ques = questions[question][0]
            options = [questions[question][1], questions[question][2], questions[question][3], questions[question][4]]
            answer = questions[question][5]
            quiz.__init__(ques, options, answer)
        return questions


class User:
    def __init__(self, username='Player', money=0.0, experience=0.0, exp_ai=0.0, exp_blockchain=0.0, exp_cloud=0.0, exp_cybersecurity=0.0,
                 exp_datascience=0.0, exp_iot=0.0, highscore_ai=0.0, highscore_blockchain=0.0, highscore_cloud=0.0, highscore_cybersecurity=0.0,
                 highscore_datascience=0.0, highscore_iot=0.0):
        self.username = username
        self.money = money
        self.experience = experience
        self.exp_ai = exp_ai
        self.exp_blockchain = exp_blockchain
        self.exp_cloud = exp_cloud
        self.exp_cybersecurity = exp_cybersecurity
        self.exp_datascience = exp_datascience
        self.exp_iot = exp_iot
        self.highscore_ai = highscore_ai
        self.highscore_blockchain = highscore_blockchain
        self.highscore_cloud = highscore_cloud
        self.highscore_cybersecurity = highscore_cybersecurity
        self.highscore_datascience = highscore_datascience
        self.highscore_iot = highscore_iot


if __name__ == '__main__':
    create_tables()
