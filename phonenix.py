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


class Phoenix(Monster):
    def __init__(self, x, y, diff):
        super().__init__(x, y, "Phoenix", 250, 500, 40, 60, 0, 40, 60, 10, 10, 10, 10, 10, 10, 3, 60, 1, 5)
        self.__diff = diff

    def get_diff(self):
        self.__diff.get()

    def take_damage(self, damage, source):
        DungeonCharacter.take_damage(self, damage, source)

        if self.get_current_hp() <= 0:
            self.rebirth()


# if __name__ == "__main__":
#     test = Phoenix(10)
#     test.take_damage(600, test)
#     print(test.get_current_hp())
#     if test.is_dead():
#         test.rebirth()
#         print(test.get_current_hp())
