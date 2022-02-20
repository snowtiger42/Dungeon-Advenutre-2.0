from abc import ABCMeta, abstractmethod
from dungeonCharacter import DungeonCharacter
import random


class Monster(DungeonCharacter):
    def __init__(self, chance_to_regenerate, regenerate_amount):
        # if self.__class__ == Monster:
        #     raise Exception('I am abstract!')
        super().__init__("Kevin", 100, 200, range(100, 200), range(100, 200), 30, 80, range(30, 80), 4, .60, .75
                         , random.uniform(.60, .75), .20, .30, random.uniform(.20, .30))
        self.__chance_to_regenerate = chance_to_regenerate
        self.__regenerate_amount = regenerate_amount


    def get_chance_to_regenerate(self):
        return self.__chance_to_regenerate

    def set_chance_to_regenerate(self):
        self.__chance_to_regenerate = random.uniform(.20, .30)

    def get_regenerate_amount(self):
        return self.__regenerate_amount

    def set_regenerate_amount(self):
        self.__regenerate_amount = random.randrange(10, 20)

    def __str__(self):
        pass

c = Monster(random.uniform(.20, .30), random.randrange(10, 20))
print(c)

