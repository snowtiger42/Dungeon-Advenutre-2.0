import sqlite3
import sqlite_creation
import sqliteinsert
import sqliteupdate
import sqliteselect


class Quiz:

    def create(self):
        database = r"dungeonquiz.db"
        sql_create_questions_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        category text NOT NULL,
                                        type text NOT NULL,
                                        question text NOT NULL
                                    ); """

        conn = sqlite_creation.create_connection(database)

        if conn is not None:
            sqlite_creation.create_table(conn, sql_create_questions_table)
        else:
            print("Error! cannot create the database connection.")

    def insert(self):
        database = r"dungeonquiz.db"

        conn = sqliteinsert.create_connection(database)
        with conn:
            project = ('Test', 'Rhetorical', 'Welcome to Die?')
            sqliteinsert.create_question(conn, project)

    def update(self):
        pass

    def select(self):
        pass


if __name__ == "__main__":
    q = Quiz()
    q.create()
    q.insert()
