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


def update_task(conn, question):
    """
    update quiz questions selected
    :param conn:
    :param question:
    :return: project id
    """
    sql = ''' UPDATE quiz
              SET category = ? ,
                  type = ? ,
                  question = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, question)
    conn.commit()

