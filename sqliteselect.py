import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_quiz(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM quiz")

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_quiz_by_priority(conn, category):
    """
    Query quiz questions by category
    :param conn: the Connection object
    :param category:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM quiz WHERE category=?", (category,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


