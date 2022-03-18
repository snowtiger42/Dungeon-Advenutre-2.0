from sqlite_creation import Connect
from sqliteinsert import Insert
from sqliteupdate import Update
from sqliteselect import Select


class SqliteMonster:

    def __init__(self):
        self.sqlite_creation = Connect()
        self.sqlite_insert = Insert()
        self.sqlite_update = Update()
        self.sqlite_select = Select()

    def create(self):
        database = r"monsters.db"

        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS monsters (
                                            monsters text PRIMARY KEY,
                                            min_hp integer NOT NULL,
                                            max_hp integer NOT NULL,
                                            attack_min integer NOT NULL,
                                            attack_max integer NOT NULL,
                                            attack_speed integer NOT NULL,
                                            chance_to_hit_min integer NOT NULL,
                                            chance_to_hit_max integer NOT NULL,
                                            chance_to_hit integer NOT NULL,
                                            chance_to_dodge_min integer NOT NULL,
                                            chance_to_regenerate_min integer NOT NULL,
                                            chance_to_regenerate_max integer NOT NULL,
                                            regenerate_amount integer NOT NULL
                                        ); """

        # create a database connection
        conn = self.sqlite_creation.create_connection(database)

        # create tables
        if conn is not None:
            # create projects table
            self.sqlite_creation.create_table(conn, sql_create_projects_table)

            # # create tasks table
            # create_table(conn, sql_create_tasks_table)
        else:
            print("Error! cannot create the database connection.")

    def insert(self):
        database = r"monsters.db"

        # create a database connection
        conn = self.sqlite_insert.create_connection(database)
        with conn:
            # create a new project
            monsters = (('emu', 250, 333, 33, 44, 3, .60, .75, .3, .5, .30, .5, 20),
                        ('phoenix', 250, 333, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20),
                        ('raven', 100, 120, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20),
                        ('sphinx', 250, 333, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20))
            project_id = self.sqlite_insert.create_project(conn, monsters)
            # for monster in monsters:
            #     project_id = create_project(conn, monster)

    def select(self):
        database = r"monsters.db"

        # create a database connection
        conn = self.sqlite_select.create_connection(database)
        with conn:
            print("1. Query task by priority:")
            self.sqlite_select.select_monster(conn, 1)

            print("2. Query all tasks")
            self.sqlite_select.select_all_tasks(conn)


if __name__ == "__main__":
    m = SqliteMonster()
    m.create()
    m.insert()
    m.select()
