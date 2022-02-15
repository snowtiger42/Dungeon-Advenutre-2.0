from abc import ABCMeta, abstractmethod
from dungeonCharacter import DungeonCharacter


class Monster(DungeonCharacter):
    @staticmethod
    @abstractmethod
    def __init__(self, chance_to_regenerate, regenerate_amount):
        if self.__class__ == Monster:
            raise Exception('I am abstract!')
        super(self.__class__, self).__init__()
        self.__chance_to_regenerate = chance_to_regenerate
        self.__regenerate_amount = regenerate_amount

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

    @staticmethod
    @abstractmethod
    def get_chance_to_regenerate(self):
        pass

    @staticmethod
    @abstractmethod
    def set_chance_to_regenerate(self):
        pass

    @staticmethod
    @abstractmethod
    def get_regenerate_amount(self):
        pass

    @staticmethod
    @abstractmethod
    def set_regenerate_amount(self):
        pass

