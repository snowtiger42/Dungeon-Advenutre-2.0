from abc import ABCMeta, abstractmethod
from abc import abstractmethod


class DungeonCharacter(object, metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def __init__(self, name, game, max_hp, current_hp, chance_to_dodge, chance_to_hit):
        if self.__class__ == DungeonCharacter:
            raise Exception('I am abstract!')
        self.__name = name
        self.__game = game
        self.__max_hp = max_hp
        self.__current_hp = current_hp
        self.__chance_to_dodge = chance_to_dodge
        self.__chance_to_hit = chance_to_hit

    @staticmethod
    @abstractmethod
    def __str__():
        pass

    @staticmethod
    @abstractmethod
    def get_name(self):
        pass

    @staticmethod
    @abstractmethod
    def set_name(self):
        pass

    @staticmethod
    @abstractmethod
    def get_hp(self):
        pass

    @staticmethod
    @abstractmethod
    def set_hp(self):
        pass

    @staticmethod
    @abstractmethod
    def get_attack_damage_range(self):
        pass

    @staticmethod
    @abstractmethod
    def set_attack_damage_range(self):
        pass

    @staticmethod
    @abstractmethod
    def get_attack_speed(self):
        pass

    @staticmethod
    @abstractmethod
    def set_attack_speed(self):
        pass

    @staticmethod
    @abstractmethod
    def get_chance_to_hit(self):
        pass

    @staticmethod
    @abstractmethod
    def set_chance_to_hit(self):
        pass

    @staticmethod
    @abstractmethod
    def get_chance_to_dodge(self):
        pass

    @staticmethod
    @abstractmethod
    def set_chance_to_dodge(self):
        pass

    @staticmethod
    @abstractmethod
    def is_dead(self):
        pass



