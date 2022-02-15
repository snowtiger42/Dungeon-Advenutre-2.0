
from abc import ABCMeta, abstractmethod
from monster import Monster
from random import randrange

class Phoenix(Monster):
    # overriding 'name' method
    def get_name(self):
        return 'Phoenix'
    # overriding 'damage_range' method
    def damage_range(self, count):
        return range(0, count)
    # overriding 'attack_speed' method
    def attack_speed(self):
        return randrange(0, 1000) # return whatever the speed is
    # overriding 'hit_chance' method
    def hit_chance(self):
        return randrange(0, 100) # return % hit chance
    # overriding 'is_dead' method
    def is_dead(self):
        monster_hp = randrange(0, 1000)
        if (monster_hp <= 0): return True
        else: return False