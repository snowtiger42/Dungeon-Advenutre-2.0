from abc import ABCMeta, abstractmethod
import random
from monster import Monster
import sqliteselect


class Phoenix(Monster):
    def __init__(self, diff, name=None, game=None):
        database = r"monsters.db"

        # create a database connection
        conn = sqliteselect.create_connection(database)
        with conn:
            print("1. Query task by priority:")
            # select_monster(conn, 'phoenix')
            monster_data = sqliteselect.select_monster(conn, 'phoenix')
        print(monster_data[6])

        super().__init__(monster_data[0], game, monster_data[1], monster_data[2], monster_data[3],
                         monster_data[4], monster_data[5], monster_data[6], monster_data[7],
                         monster_data[8], monster_data[9], monster_data[10], monster_data[11], monster_data[12])
        # self.__game = game
        self.__diff = diff
        # self.__name = name

    def get_diff(self):
        self.__diff.get()

    # overriding 'name' method
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = "Phoenix"


if __name__ == "__main__":
    test = Phoenix(10)
# p = Phoenix(1, "Phoenix", Game())
# print(p)
#
# p.take_damage(1000, "Hero")
#
# print(p)
#
# p.regenerate()
# p.regenerate()
# p.regenerate()
#
# print(p)

# print("\n------------------------print adventurer status (TIME TO DIE!!!)-------------------------")
# print(p)
# p.take_damage(2000, "extra legendary pit")
# print(p)

