import sqlite_creation
import sqliteinsert
import sqliteupdate
import sqliteselect


class Quiz:
    def create(self):
        database = r"dungeonquiz.db"
        sql_create_questions_table = """ CREATE TABLE IF NOT EXISTS quiz (
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
            question_1 = ('Test', 'Rhetorical', 'Welcome to Die?')
            question_2 = ('Test', 'Non-Rhetorical', 'Papa can you hear me?')
            sqliteinsert.create_question(conn, question_1)
            sqliteinsert.create_question(conn, question_2)

    def update(self):
        database = r"dungeonquiz.db"

        conn = sqliteupdate.create_connection(database)
        with conn:
            sqliteupdate.update_task(conn, (1, 'Test', 'Rhetorical', 'Welcome to Die?'))

        print('done')

    def select(self):
        database = r"dungeonquiz.db"

        # create a database connection
        conn = sqliteselect.create_connection(database)
        with conn:
            print("1. Query questions by category:")
            sqliteselect.select_quiz_by_priority(conn, 'Rhetorical')
            sqliteselect.select_quiz_by_priority(conn, 'Non-Rhetorical')

            print("2. Query all questions")
            sqliteselect.select_all_quiz(conn)


if __name__ == "__main__":
    q = Quiz()
    q.create()
    q.insert()
    q.select()
    q.update()
