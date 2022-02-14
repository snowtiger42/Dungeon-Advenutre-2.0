from abc import ABCMeta, abstractmethod
from dungeonCharacter import DungeonCharacter


class Monster(metaclass=ABCMeta, DungeonCharacter):

    @staticmethod
    @abstractmethod
    def get_name(self):
        pass

    @staticmethod
    @abstractmethod
    def damage_range(self):
        pass

    @staticmethod
    @abstractmethod
    def attack_speed(self):
        pass

    @staticmethod
    @abstractmethod
    def hit_chance(self):
        pass

    @staticmethod
    @abstractmethod
    def is_dead(self):
        pass