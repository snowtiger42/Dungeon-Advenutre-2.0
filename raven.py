from abc import ABCMeta, abstractmethod
import random

from dungeonCharacter import DungeonCharacter
from monster import Monster
from mock_game import MockGame as Game


"""
self, name, min_hp, max_hp, generated_hp, current_hp, attack_min, attack_max, attack_damage_range,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_hit, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_dodge, chance_to_regenerate_min, chance_to_regenerate_max,
                 regenerate_amount
"""
class Raven(Monster):
    def __init__(self, diff, name, game):
        super().__init__(name, game, 100, 120, 40, 60, 1, .40, .60, .10, .25, .10, .20, 20)
        self.__game = game
        self.__diff = diff
        self.__name = name

    def get_diff(self):
        self.__diff.get()

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = "Raven"

# jack = Raven(1, "Raven", Game())
# jill = Raven(1, "Raven", Game())
# jack.fight(jack, jill)


    # def __str__(self):
    #     self.__game.announcement(f"{super().__str__()}")


# a = Raven(1, "Raven", Game())
# print(a)
# if __name__ == "__main__":
#     test = Raven(10)
#     test.take_damage(500, test)
#     if test.is_dead():
#         print(test.get_current_hp())


