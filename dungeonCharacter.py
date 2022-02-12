from abc import ABCMeta, abstractmethod
from abc import abstractmethod


class DungeonCharacter(metaclass=ABCMeta):

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


