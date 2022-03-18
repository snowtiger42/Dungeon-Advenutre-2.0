import sqlite3
from sqlite3 import Error


class Select:
    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def selected_quiz(rows):
        return rows

    @staticmethod
    def select_all_tasks(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM monsters")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    @staticmethod
    def select_monster(conn, monster):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param monster: String emu, sphinx, phoenix, raven
        :return:
        """
        cur = conn.cursor()
        cur.execute("""SELECT * FROM monsters WHERE monsters=?""", (monster,))
        # I think so
        #
        rows = cur.fetchall()
        # create a function to query for each monster
        # pass in a specific variable and then query the monster name is a better version
        for row in rows:
            return row
