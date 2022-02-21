import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_question(conn, question):
    """
    Create a new project into the projects table
    :param conn:
    :param question:
    :return: project id
    """
    sql = ''' INSERT INTO projects(category, type, question)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, question)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"mysqlitedb.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        create_question(conn, project)


if __name__ == '__main__':
    main()
