from abc import ABCMeta, abstractmethod
import random
from dungeonCharacter import DungeonCharacter
from monster import Monster
import sqliteselect

"""
self, name, min_hp, max_hp, generated_hp, current_hp, attack_min, attack_max, attack_damage_range,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_hit, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_dodge, chance_to_regenerate_min, chance_to_regenerate_max,
                 regenerate_amount
"""


class Raven(Monster):
    def __init__(self, diff, name='raven', game=None):  # use db query
        database = r"monsters.db"

        # create a database connection
        conn = sqliteselect.create_connection(database)
        with conn:
            print("1. Query task by priority:")
            # select_monster(conn, 'raven')
            monster_data = sqliteselect.select_monster(conn, 'raven')
        print(monster_data[1])

        super().__init__("Raven", game, 100, 120, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20)
        self.__diff = diff

    def get_diff(self):
        self.__diff.get()

        # overriding 'name' method

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = "Raven"


if __name__ == "__main__":
    test = Raven(10)
#     test.take_damage(500, test)
#     if test.is_dead():
#         print(test.get_current_hp())


