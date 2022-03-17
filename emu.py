from abc import ABCMeta, abstractmethod
import random
from dungeonCharacter import DungeonCharacter
from monster import Monster
import sqliteselect_monsters

"""
self, name, game, min_hp, max_hp, attack_min, attack_max, \
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_regenerate_min, chance_to_regenerate_max,
                 regenerate_amount
"""


class Emu(Monster):
    def __init__(self, diff, name=None, game=None):
        database = r"monsters.db"

        # create a database connection
        conn = sqliteselect.create_connection(database)
        with conn:
            print("1. Query task by priority:")
            # select_monster(conn, 'emu')
            monster_data = sqliteselect.select_monster(conn, 'emu')
        print(monster_data[0]) # access each number individually

        super().__init__(monster_data[0], game, monster_data[1], monster_data[2], monster_data[3],
                         monster_data[4], monster_data[5], monster_data[6], monster_data[7],
                         monster_data[8], monster_data[9], monster_data[10], monster_data[11], monster_data[12])
        self.__diff = diff
        # self.__name = name

    def get_diff(self):
        self.__diff.get()

    # overriding 'name' method
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = "Emu"

    # def take_damage(self, damage, source):
    #     self.__game.announce(f"{self.__name} took {damage} dmg from {source}!\n{self.__name} are now at "
    #                          f"{self.get_current_hp()} hp!")

    # def __str__(self):
    #     super().__str__()


if __name__ == "__main__":
    test = Emu(10)
#     test.take_damage(500, test)
#     if test.is_dead():
#         print(test.get_current_hp())


