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


def select_quiz_by_priority(conn, id):
    """
    Query quiz questions by category
    :param conn: the Connection object
    :param id:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM quiz WHERE id=?", (id,))

    rows = cur.fetchone()
    return rows


def selected_quiz(rows):
    return rows
