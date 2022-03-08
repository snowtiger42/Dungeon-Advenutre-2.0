from abc import ABCMeta, abstractmethod
import random
from monster import Monster


class Phoenix(Monster):
    def __init__(self, diff, name):
        super().__init__(name, 250, 333, 33, 44, 3, .60, .75, random.uniform(.60, .75), .3, .5, random.uniform(.3, .5),
                         .30, .5, 20)
        self.__diff = diff
        self.__name = name

    def get_attack_damage_range(self):
        super().get_attack_damage_range()

    def get_diff(self):
        self.__diff.get()

    # overriding 'name' method
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = "Phoenix"


# p = Phoenix(1, "Phoenix")
# print(p)
#
# p.take_damage(100, "Hero")
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

