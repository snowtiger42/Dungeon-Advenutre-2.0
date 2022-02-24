from abc import ABCMeta, abstractmethod
from dungeonCharacter import DungeonCharacter

<<<<<<< Updated upstream

class Monster(metaclass=ABCMeta, DungeonCharacter):
=======
"""
self, name, min_hp, max_hp, attack_min, attack_max,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_dodge_min,
                 chance_to_dodge_max
"""
class Monster(DungeonCharacter):
    def __init__(self, name, min_hp, max_hp, attack_min, attack_max,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_regenerate_min, chance_to_regenerate_max):
        # don't need generated_hp, current_hp, attack_damage_range, chance_to_hit
        # chance_to_dodge or regenerate_amount passed in as arguments
        # they are derived from other statistics
        # if self.__class__ == Monster:
        #     raise Exception('I am abstract!')
        super().__init__(name, min_hp, max_hp, attack_min, attack_max,
                         attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_dodge_min,
                         chance_to_dodge_max)
        # don't need generated_hp, current_hp passed, attack_damage_range, chance_to_hit
        # chance_to_dodge or regenerate_amount passed in as arguments
>>>>>>> Stashed changes

    @staticmethod
    @abstractmethod
    def get_name(self):
        pass

<<<<<<< Updated upstream
    @staticmethod
    @abstractmethod
    def damage_range(self):
        pass
=======
        self.__chance_to_regenerate = random.uniform(self.__chance_to_regenerate_min, self.__chance_to_regenerate_max)
        self.__regenerate_amount = 10
>>>>>>> Stashed changes

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