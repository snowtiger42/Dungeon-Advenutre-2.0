from abc import ABCMeta, abstractmethod
import random
from monster import Monster


class Phoenix(Monster):
    def __init__(self, diff, name):
        super().__init__(name, 250, 333, range(250, 333), range(250, 333), 33, 44, range(33, 44), 3, .60,
                         .75, random.uniform(.60, .75), .3, .5, random.uniform(.3, .5), .30, .5, 20)
        self.__diff = diff
        self.__name = name

    def get_diff(self):
        self.__diff.get()

    # overriding 'name' method
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = "Phoenix"

    # overriding 'is_dead' method
    def is_dead(self):
        if self.__current_hp <= 0:
            return self.__current_hp <= 0
        else:
            return False

    # def __str__(self):
    #     prefix = super().__str__()
    #     p = format(prefix)
    #     return print(p)

p = Phoenix(1, "Phoenix")
print(p)
