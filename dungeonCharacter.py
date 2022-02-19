from abc import ABCMeta, abstractmethod
from abc import abstractmethod
from mock_game import MockGame as Game
import sys
import random
import numpy as np



class DungeonCharacter(object, metaclass=ABCMeta):
# class DungeonCharacter:

    def __init__(self, name, min_hp, max_hp, generated_hp, current_hp, attack_min, attack_max, attack_damage_range
                 , attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_hit, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_dodge):
        # if self.__class__ == DungeonCharacter:
        #     raise Exception('I am abstract!')
        self.__name = name
        # self.__game = game
        self.__min_hp = min_hp
        self.__max_hp = max_hp

        self.__generated_hp = random.randrange(self.__min_hp, self.__max_hp)
        self.__current_hp = self.__generated_hp
        # self.__generated_hp = generated_hp
        # self.__current_hp = current_hp
        self.__attack_min = attack_min
        self.__attack_max = attack_max

        self.__attack_damage_range = random.randrange(self.__attack_min, self.__attack_max)
        # self.__attack_damage_range = attack_damage_range
        self.__attack_speed = attack_speed
        self.__chance_to_dodge_min = chance_to_dodge_min
        self.__chance_to_dodge_max = chance_to_dodge_max
        self.__chance_to_dodge = chance_to_dodge
        self.__chance_to_hit_min = chance_to_hit_min
        self.__chance_to_hit_max = chance_to_hit_max
        self.__chance_to_hit = chance_to_hit

    def get_min_hp(self):
        return self.__min_hp

    def set_min_hp(self):
        self.__min_hp = 100

    def get_max_hp(self):
        return self.__max_hp

    def set_max_hp(self):
        self.__max_hp = 200

    # def get_generated_hp(self):
    #     return self.__generated_hp
    #
    # def set_generated_hp(self):
    #     self.__generated_hp = range(int(self.__min_hp), int(self.__max_hp))
    #
    # def get_current_hp(self):
    #     return self.__current_hp
    #
    # def set_current_hp(self):
    #     self.__current_hp = self.__generated_hp

    def get_attack_min(self):
        return self.__attack_min

    def set_attack_min(self):
        self.__attack_min = 30

    def get_attack_max(self):
        return self.__attack_max

    def set_attack_max(self):
        self.__attack_max = 80

    def get_attack_damage_range(self):
        return self.__attack_damage_range

    def set_attack_damage_range(self):
        self.__attack_damage_range = random.uniform(self.__attack_min, self.__attack_max)

    def get_attack_speed(self):
        return self.__attack_speed

    def set_attack_speed(self):
        self.__attack_speed = 4

    def get_chance_to_hit_min(self):
        return self.__chance_to_hit_min

    def set_chance_to_hit_min(self):
        self.__chance_to_hit_min = .60

    def get_chance_to_hit_max(self):
        return self.__chance_to_hit_max

    def set_chance_to_hit_max(self):
        self.__chance_to_hit_max = .75

    def get_chance_to_hit(self):
        return self.__chance_to_hit

    def set_chance_to_hit(self):
        self.__chance_to_hit = random.uniform(self.__chance_to_hit_min, self.__chance_to_hit_max)

    def get_chance_to_dodge_max(self):
        return self.__chance_to_dodge_max

    def set_chance_to_dodge_max(self):
        self.__chance_to_dodge_max = .30

    def get_chance_to_dodge_min(self):
        return self.__chance_to_dodge_min

    def set_chance_to_dodge_min(self):
        self.__chance_to_dodge_min = .20

    def get_chance_to_dodge(self):
        return self.__chance_to_dodge

    def set_chance_to_dodge(self):
        self.__chance_to_dodge = random.uniform(self.__chance_to_dodge_min, self.__chance_to_dodge_max)

    # @abstractmethod
    # def __str__():
    #     pass

    def get_name(self):
        """
        Getter for name property.
        """
        return str(self.__name)

    def set_name(self, name):
        self.__name = name

    def is_dead(self):
        """
        Returns true if the adventurer's HP is above 0, and False otherwise.
        """
        return (self.__current_hp <= 0), sys.exit()


    def attack(self):
        pass

    def take_damage(self, damage, source):
        """
        Reduces HP by the indicated amount and makes an announcement.
        """
        self.__current_hp -= damage
        print(f"Oh no! {self.__name} took {damage} dmg from {source}!\nThey are now at {self.__current_hp} hp!")

        # self.__game.announce(f"Oh no! {self.__name} took {damage} dmg from {source}!\nThey are now at {self.__current_hp} hp!")

    # @abstractmethod
    def __str__(self):
        """
        Returns a string representation of the Adventurer.
        """

        # produce a content line for each status item
        name_str = f"Name: {self.__name}"
        hp_str = f"HP: {self.__current_hp} / {self.__generated_hp}"
        attack_str = f"Attack Range: {self.__attack_min} to {self.__attack_max}"
        speed_str = f"Speed: {self.__attack_speed}"
        dodge_str = f"Dodge Chance: {round(self.__chance_to_dodge_min * 100)}% to {round(self.__chance_to_dodge_max * 100)}% "
        accuracy_str = f"Hit Chance: {round(self.__chance_to_hit_min * 100)}% to {round(self.__chance_to_hit_max * 100)}%"

        # dodge_str = f"Dodge Chance: {round(self.__chance_to_dodge * 100, 2)}%"
        # accuracy_str = f"Hit Chance: {round(self.__chance_to_hit * 100, 2)}%"

        # return name_str, hp_str, attack_str, speed_str, dodge_str, accuracy_str


        # healthp_str = f"Health potions: {self.__health_p}"
        # visionp_str = f"Vision potions: {self.__vision_p}"
        # pillar_string = f"Pillars found: {self.__pillars}"

        status_items = [name_str, hp_str, attack_str, speed_str, dodge_str, accuracy_str]
        # return status_items
        # # a = status_items

        # find the longest status item and get its length
        line_size = 0
        for line in status_items:
            if len(line) > line_size:
                line_size = len(line)

        # create borders
        border = "+" + "-" * (line_size + 2) + "+"

        # add spacers to all status items based on max length
        # so that right border is even
        output_str = "\n" + border
        for line in status_items:
            output_str += f"\n| {line}"
            white_space = line_size - len(line)
            if white_space > 0:
                output_str += " " * white_space
            output_str += " |"

        output_str += f"\n{border}\n"

        return output_str



a = DungeonCharacter("Kevin", 100, 200, range(100, 200), range(100, 200), 30, 80, range(30, 80), 4, .60, .75,
                     random.uniform(.60, .75), .20, .30, random.uniform(.20, .30))

print(a)
