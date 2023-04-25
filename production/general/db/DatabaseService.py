"""
This database service class provides the ability to add, delete, update and select against a SQLite database,
corresponding to four methods that the developer can call and follow the instructions in the method to achieve the
functionality.
A method is provided to create all tables needed in the database, which will be called at the start of the program.

Written by Zhongjie Huang
Last modified: 24/4/2023
"""

import sqlite3


def insert_data(table_name, columns, values):
    """
    This function is used to insert data into a table, taking three parameters, which are table name, columns name and
    values corresponding to the columns name.
    For example:
        insert_data("HOUSES", "HOUSE_ID", "3")
    You can add multiple column names and values:
        insert_data("HOUSES", "HOUSE_ID, HOUSE_NUMBER", "3, 4")
    If the value is non-numeric, you need to add single quotes:
        insert_data("HOUSES", "HOUSE_DESCRIPTION", "'house'")
    You can only add a whole row!
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        insert_data_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        try:
            cursor.execute(insert_data_query)
            connection.commit()
            print(f"A row contains columns: ({columns}) in table: ({table_name}) has been added successfully "
                  f"with values: ({values})")
        except sqlite3.Error as e:
            print("An error occurred: ", e)
            connection.rollback()


def delete_data(table_name, conditions):
    """
    This function is used to delete data from a table, taking two parameters, which are table name and conditions.
    For example:
        delete_data("HOUSES", "ID = 1")
    If the assigned value is non-numeric, you need to add single quotes:
        delete_data("HOUSES", "ID = 1 AND HOUSE_NAME = 'AI'")
    You can only delete a whole row!
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        delete_data_query = f"DELETE FROM {table_name} WHERE {conditions}"
        try:
            cursor.execute(delete_data_query)
            connection.commit()
            print(f"Rows in table: ({table_name}) with conditions: ({conditions}) have been deleted successfully")
        except sqlite3.Error as e:
            print("An error occurred: ", e)
            connection.rollback()


def update_data(table_name, columns_set, conditions):
    """
    This function is used to update the data on a table, taking three parameters, which are table name, columns set
    and conditions.
    For example:
        update_data("HOUSES", "HOUSE_NUMBER = 10", "ID = 1")
    You can choose not to have a condition, in this case you must set the condition to None:
        update_data("HOUSES", "HOUSE_NUMBER = 10", None)
    If the assigned value is non-numeric, you need to add single quotes:
        update_data("HOUSES", "HOUSE_NUMBER = 10, HOUSE_NAME = 'AI'", "ID = 1")
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        if conditions:
            update_data_query = f"UPDATE {table_name} SET {columns_set} WHERE {conditions}"
        else:
            update_data_query = f"UPDATE {table_name} SET {columns_set}"
        try:
            cursor.execute(update_data_query)
            connection.commit()
            print(f"Rows in table: ({table_name}) with conditions: ({conditions}) have been updated successfully with "
                  f"columns_set: ({columns_set})")
        except sqlite3.Error as e:
            print("An error occurred: ", e)
            connection.rollback()


def select_data(table_name, columns, conditions):
    """
    This function is used to select the data from a table, taking three parameters, which are table name, columns and
    conditions.
    For example:
        select_data("HOUSES", "HOUSE_NUMBER, HOUSE_NAME", "ID = 1")
    You can choose not to have a condition, in this case you must set the condition to None:
        select_data("HOUSES", "HOUSE_NUMBER, HOUSE_NAME", None)
    You can select all columns at once:
        select_data("HOUSES", "*", None)
    If the assigned value is non-numeric, you need to add single quotes:
        select_data("HOUSES", "HOUSE_NUMBER", "HOUSE_NAME = 'AI'")
    The returned results are in a list and tuple, you need to used index to get it.
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        if conditions:
            select_data_query = f"SELECT {columns} FROM {table_name} WHERE {conditions}"
        else:
            select_data_query = f"SELECT {columns} FROM {table_name}"
        data_results = None
        try:
            cursor.execute(select_data_query)
            data_results = cursor.fetchall()
            print(f"Rows in table: ({table_name}) with conditions: ({conditions}) have been selected successfully "
                  f"with columns: ({columns})")
        except sqlite3.Error as e:
            print("An error occurred: ", e)
    return data_results


def create_all_tables():
    """
    This function is used to create all tables and should be called in the launch part of the game program.
    """
    with sqlite3.connect('AIGame.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''CREATE TABLE IF NOT EXISTS Table_name (
                              ID INTEGER PRIMARY KEY AUTOINCREMENT);''')
            connection.commit()
        except sqlite3.Error as e:
            print("An error occurred: ", e)
            connection.rollback()


insert_data("HOUSES", "HOUSE_NAME, HOUSE_DESCRIPTION", "'AI', 'AII'")
