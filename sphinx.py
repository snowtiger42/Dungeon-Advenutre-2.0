<<<<<<< Updated upstream
class Sphinx(Monster):
    def __init__(self, diff):
        super(self.__class__, self).__init__()
=======
from abc import ABCMeta, abstractmethod
import random
from monster import Monster

"""
self, name, min_hp, max_hp, attack_min, attack_max,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_regenerate_min, chance_to_regenerate_max
"""


class Sphinx(Monster):
    def __init__(self, diff):
        super().__init__("Sphinx", 250, 333, 10, 10, 10, 10, 10, 10, 10, 1, 2)
>>>>>>> Stashed changes
        self.__diff = diff

    def get_diff(self):
        self.__diff.get()

<<<<<<< Updated upstream
    def get_hp(self):
        self.__max_hp = self.__current_hp
        return self.__max_hp

    def set_hp(self):
        self.__current_hp = 333 * self.__diff

    def get_attack_damage_range(self):
        return self.__attack_damage_range

    def set_attack_damage_range(self):
        self.__attack_damage_range = random.randrange(25, 50)

    def get_attack_speed(self):
        return self.__attack_speed

    def set_attack_speed(self):
        self.__attack_speed = (3 + self.__diff)

    def get_chance_to_hit(self):
        return self.__chance_to_hit

    def set_chance_to_hit(self):
        self.__chance_to_hit = random.uniform(.30, .50) + (self.__diff / 10)

    def get_chance_to_dodge(self):
        return self.__chance_to_dodge

    def set_chance_to_dodge(self):
        self.__chance_to_dodge = random.uniform(.10, .20) * self.__diff

    def get_chance_to_regenerate(self):
        return self.__chance_to_regenerate

    def set_chance_to_regenerate(self):
        self.__chance_to_regenerate = random.uniform(.10, .20) * self.__diff

    def get_regenerate_amount(self):
        return self.__regenerate_amount

    def set_regenerate_amount(self):
        self.__regenerate_amount = random.randrange(20, 40) * self.__diff

    def regenerate_hp(self):
        regenerate = self.__regenerate_amount
        regenerate += self.__current_hp

        self.__game.announce(f"Regenerated! It heals {regenerate} HP, bringing it to {self.__current_hp}/{self.__max_hp}.")

    # overriding 'name' method
    def get_name(self):
        return 'Sphinx'

    # overriding 'is_dead' method

    def is_dead(self):
        if self.__current_hp <= 0:
            return self.__current_hp <= 0
        else:
            return False

from abc import ABCMeta, abstractmethod
# from monster import Monster
from random import randrange

# class Sphinx(Monster):
    # overriding 'name' method
def get_name(self):
    return 'Phoenix'
# overriding 'damage_range' method
def damage_range(self, count):
    return range(0, count)
# overriding 'attack_speed' method
def attack_speed(self):
    return randrange(0, 1) # return whatever the speed is
# overriding 'hit_chance' method
def hit_chance(self):
    return randrange(0, 100) # return % hit chance
# overriding 'is_dead' method
def is_dead(self):
    monster_hp = randrange(0, 1000)
    if (monster_hp <= 0): return True
    else: return False
=======

if __name__ == "__main__":
    test = Sphinx(10)
    test.take_damage(500, test)
        
    # p = Sphinx(1, "Sphinx")
    # print(p)

    # overriding 'name' method
    # def get_name(self):
    #     return self.__name
    # 
    # def set_name(self, name):
    #     self.__name = "Sphinx"

    # overriding 'is_dead' method
    # def is_dead(self):
    #     if self.__current_hp <= 0:
    #         return self.__current_hp <= 0
    #     else:
    #         return False

    # def __str__(self):
    #     prefix = super().__str__()
    #     p = format(prefix)
    #     return print(p)


>>>>>>> Stashed changes
