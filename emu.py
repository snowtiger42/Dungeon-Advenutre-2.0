from abc import ABCMeta, abstractmethod
import random
from mock_game import MockGame as Game
from dungeonCharacter import DungeonCharacter
from monster import Monster

"""
self, name, game, min_hp, max_hp, attack_min, attack_max, \
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_regenerate_min, chance_to_regenerate_max,
                 regenerate_amount
"""


class Emu(Monster):
    def __init__(self, diff, name, game):
        super().__init__(name, game, 100, 200, 40, 60, 1, .40, .60, .10, .25, .50, .60, 20)
        self.__game = game
        self.__diff = diff
        self.__name = name

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


# if __name__ == "__main__":
#     test = Emu(10)
#     test.take_damage(500, test)
#     if test.is_dead():
#         print(test.get_current_hp())


