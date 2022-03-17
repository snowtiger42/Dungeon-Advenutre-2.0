
from abc import ABCMeta, abstractmethod
import random

from dungeonCharacter import DungeonCharacter
from monster import Monster

"""
self, name, min_hp, max_hp, generated_hp, current_hp, attack_min, attack_max, attack_damage_range,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_hit, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_dodge, chance_to_regenerate_min, chance_to_regenerate_max,
                 regenerate_amount
"""


class Sphinx(Monster):
    def __init__(self, diff, name, game):
        super().__init__(name, game, 250, 333, 33, 44, 3, .60, .75, .3, .5, .30, .5, 20)
        self.__game = game
        self.__diff = diff
        self.__name = name

    def get_diff(self):
        self.__diff.get()

    # overriding 'name' method
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = "Sphinx"


# if __name__ == "__main__":
#     test = Sphinx(10)
#     test.take_damage(500, test)
#     if test.is_dead():
#         print(test.get_current_hp())
