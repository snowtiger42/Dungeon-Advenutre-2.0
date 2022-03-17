from abc import ABCMeta, abstractmethod
# from abc import abstractmethod
from mock_game import MockGame as Game

# import sys
import random

# from practice_gui import Practice_gui
# from battleground import Battleground
from mockannouncement import MockAnnouncement as Announce



class DungeonCharacter(object, metaclass=ABCMeta):

    def __init__(self, name, game, min_hp, max_hp, attack_min, attack_max, attack_speed, chance_to_hit_min,
                 chance_to_hit_max, chance_to_dodge_min, chance_to_dodge_max):
        # if self.__class__ == DungeonCharacter:
        #     raise Exception('I am abstract!')
        self.__name = name
        self.__game = game
        self.__min_hp = min_hp
        self.__max_hp = max_hp

        # self.battleground = Battleground()
        self.announce = Announce()

        self.__generated_hp = random.randrange(self.__min_hp, self.__max_hp)
        self.__current_hp = self.__generated_hp
        self.__attack_min = attack_min
        self.__attack_max = attack_max

        self.__attack_damage_range = random.randrange(self.__attack_min, self.__attack_max)
        self.__attack_speed = attack_speed
        self.__chance_to_dodge_min = chance_to_dodge_min
        self.__chance_to_dodge_max = chance_to_dodge_max
        self.__chance_to_dodge = random.uniform(self.__chance_to_dodge_min, self.__chance_to_dodge_max)
        self.__chance_to_hit_min = chance_to_hit_min
        self.__chance_to_hit_max = chance_to_hit_max
        # self.__chance_to_hit = chance_to_hit
        self.__chance_to_hit = random.uniform(self.__chance_to_hit_min, self.__chance_to_hit_max)

    def set_game(self):
        self.__game = Game()

    def get_game(self):
        return self.__game

    def get_min_hp(self):
        return self.__min_hp

    def set_min_hp(self, min_hp):
        self.__min_hp = min_hp

    def get_max_hp(self):
        return self.__max_hp

    def set_max_hp(self, max_hp):
        self.__max_hp = max_hp

    def get_generated_hp(self):
        return self.__generated_hp

    def set_generated_hp(self, hp):
        self.__generated_hp = hp

    def get_current_hp(self):
        return self.__current_hp

    def set_current_hp(self, new_hp):
        self.__current_hp = new_hp

    def get_attack_min(self):
        return self.__attack_min

    def set_attack_min(self, attack_min):
        self.__attack_min = attack_min

    def get_attack_max(self):
        return self.__attack_max

    def set_attack_max(self, attack_max):
        self.__attack_max = attack_max

    def get_attack_damage_range(self):
        return self.__attack_damage_range

    def set_attack_damage_range(self, damage_rate):
        self.__attack_damage_range = damage_rate

    def get_attack_speed(self):
        return self.__attack_speed

    def set_attack_speed(self, speed):
        self.__attack_speed = speed

    def get_chance_to_hit_min(self):
        return self.__chance_to_hit_min

    def set_chance_to_hit_min(self, hit_min):
        self.__chance_to_hit_min = hit_min

    def get_chance_to_hit_max(self):
        return self.__chance_to_hit_max

    def set_chance_to_hit_max(self, hit_max):
        self.__chance_to_hit_max = hit_max

    def get_chance_to_hit(self):
        return self.__chance_to_hit

    def set_chance_to_hit(self, hit_chance):
        self.__chance_to_hit = hit_chance

    def get_chance_to_dodge_max(self):
        return self.__chance_to_dodge_max

    def set_chance_to_dodge_max(self, dodge_max):
        self.__chance_to_dodge_max = dodge_max

    def get_chance_to_dodge_min(self):
        return self.__chance_to_dodge_min

    def set_chance_to_dodge_min(self, dodge_min):
        self.__chance_to_dodge_min = dodge_min

    def get_chance_to_dodge(self):
        return self.__chance_to_dodge

    def set_chance_to_dodge(self, chance_to_dodge):
        self.__chance_to_dodge = chance_to_dodge

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
        return self.get_current_hp() <= 0

    def take_damage(self, damage, source):
        """
        Reduces HP by the indicated amount and makes an announcement.
        """
        announcement = self.announce
        self.__current_hp = self.get_current_hp() - damage

        if self.__current_hp <= 0:
            self.set_current_hp(0)
            self.is_dead()

        # print(f"Oh no! {self.__name} took {damage} dmg from {source}!\nThey are now at {self.__current_hp} hp!")
        self.__game.announce(f"{self.__name} took {damage} dmg from {source}!\n{self.__name} are now at "
                             f"{self.get_current_hp()} hp!")

        announcement.announce(f"{self.__name} took {damage} dmg from {source}!\n{self.__name} are now at "
                             f"{self.get_current_hp()} hp!")

        # determines whether an attack is a hit or a miss. Returns true if attack is successful.
        # Generates random number. Compares random number to attack chance.

    def fight(self, attacker, defender):
        announcement = self.announce

        attacker_damage = random.randint(attacker.get_attack_min(), attacker.get_attack_max())
        defender_new_hp = defender.get_current_hp()

        defender_damage = random.randint(defender.get_attack_min(), defender.get_attack_max())
        attacker_new_hp = attacker.get_current_hp()

        dodge_chance = random.uniform(.1, 1)
        hit_chance = random.uniform(.1, 1)  # generates a random % chance of a successful attack by this character
        if attacker.get_attack_speed() >= defender.get_attack_speed():
            """Conditions placed here depending on button press"""

            if attacker.get_chance_to_hit() >= hit_chance:
                if defender.get_chance_to_dodge() < dodge_chance:
                    defender.take_damage(attacker_damage, attacker.get_name())
                    announcement.announce_monster_stats(f"{defender}") #make a reference to battleground
                else:
                    announcement.announce(f"{attacker.get_name()} has missed resulting in {0} damage to {defender.get_name()} hp."
                          f" {defender.get_name()} has {defender.get_current_hp()} hp.\n")
            else:
                announcement.announce(f"{attacker.get_name()} has missed resulting in {0} damage to {defender.get_name()} hp."
                                     f" {defender.get_name()} has {defender.get_current_hp()} hp.\n")

            if defender.get_current_hp() > 0:
                if defender.get_chance_to_hit() >= hit_chance:
                    if attacker.get_chance_to_dodge() < dodge_chance:
                        attacker.take_damage(defender_damage, defender.get_name())
                        announcement.announce_hero_stats(f"{attacker}")

                    else:
                        announcement.announce(f"{defender.get_name()} has missed resulting in {0} damage to {attacker.get_name()} hp."
                              f" {attacker.get_name()} has {attacker.get_current_hp()} hp.\n")
                else:
                    announcement.announce(f"{defender.get_name()} has missed resulting in {0} damage to {attacker.get_name()} hp."
                                         f" {attacker.get_name()} has {attacker.get_current_hp()} hp.\n")



    # """Move most of this to DA_class and create GUI, The GUI must have buttons fight, use_potion, special move. the buttons will have conditions where if a button is pressed that action will
    # take place; elif another button is pressed, then that action happens. Then the monster will recipricate by striking"""
    # def combat(self, attacker, defender):
    #     "Note. Get rid of the while statement when making a GUI!!!"
    #     # while defender.get_current_hp() > 0 and attacker.get_current_hp() > 0:
    #     # attacker_damage = attacker.get_attack_damage_range()
    #     attacker_damage = random.randint(attacker.get_attack_min(), attacker.get_attack_max())
    #     defender_new_hp = defender.get_current_hp(self)
    #
    #     defender_damage = random.randint(defender.get_attack_min(self), defender.get_attack_max(self))
    #     attacker_new_hp = attacker.get_current_hp()
    #
    #     attcker_result = defender_new_hp - attacker_damage
    #     defender_result = attacker_new_hp - defender_damage
    #
    #     dodge_chance = random.uniform(.1, 1)
    #     # character will attack another character
    #     hit_chance = random.uniform(.1, 1)  # generates a random % chance of a successful attack by this character
    #     if attacker.get_attack_speed() >= defender.get_attack_speed():
    #         """Conditions placed here depending on button press"""
    #
    #         if attacker.get_chance_to_hit() >= hit_chance:
    #             if defender.get_chance_to_dodge() < dodge_chance:
    #                 defender.set_current_hp(defender.get_current_hp() - attacker_damage)                            #make set to take_damage
    #                 self.__game.announce(f"The {attacker} has dealt the {defender} {attacker_damage} damage to "
    #                                      f"their hp. The {defender} has {defender.get_current_hp()} hp.")
    #             else:
    #                 self.__game.announce(f"The {attacker} has missed resulting in {0} damage to {defender} hp."
    #                                      f"The {defender} has {defender.get_current_hp()} hp.")
    #         else:
    #             self.__game.announce(f"The {attacker} has missed resulting in {0} damage to {defender} hp."
    #                                  f"The {defender} has {defender.get_current_hp()} hp.")
    #
    #         if defender.get_current_hp() > 0:
    #             if defender.get_chance_to_hit() >= hit_chance:
    #                 if attacker.get_chance_to_dodge() < dodge_chance:
    #                     attacker.set_current_hp(attacker.get_current_hp() - defender_damage)
    #                     self.__game.announce(f"The {defender} has dealt the {attacker} {defender_damage} damage to"
    #                                          f" their hp. The {attacker} has {attacker.get_current_hp()} hp.")
    #                 else:
    #                     self.__game.announce(f"The {defender} has missed resulting in {0} damage to {attacker} hp."
    #                                          f"The {attacker} has {attacker.get_current_hp()} hp.")
    #             else:
    #                 self.__game.announce(f"The {defender} has missed resulting in {0} damage to {attacker} hp."
    #                                      f"The {attacker} has {attacker.get_current_hp()} hp.")
    #
    #     elif attacker.get_attack_speed() < defender.get_attack_speed():
    #         if defender.get_chance_to_hit() >= hit_chance:
    #             if attacker.get_chance_to_dodge() < dodge_chance:
    #                 attacker.set_current_hp(attacker.get_current_hp() - defender_damage)
    #                 self.__game.announce(f"The {defender} has dealt the {attacker} {defender_damage} damage to "
    #                                      f"their hp. The {attacker} has {attacker.get_current_hp()} hp.")
    #             else:
    #                 self.__game.announce(f"The {defender} has missed resulting in {0} damage to {attacker} hp."
    #                                      f"The {attacker} has {attacker.get_current_hp()} hp.")
    #         else:
    #             self.__game.announce(f"The {defender} has missed resulting in {0} damage to {attacker} hp."
    #                                  f"The {attacker} has {attacker.get_current_hp()} hp.")
    #
    #
    #         """Conditions placed here depending on button press"""
    #         if attacker.get_current_hp() > 0:
    #             if attacker.get_chance_to_hit() >= hit_chance:
    #                 if defender.get_chance_to_dodge() < dodge_chance:
    #                     defender.set_current_hp(defender.get_current_hp() - attacker_damage)
    #                     self.__game.announce(f"The {attacker} has dealt the {defender} {attacker_damage} damage to"
    #                                          f" their hp. The {defender} has {defender.get_current_hp()} hp.")
    #                 else:
    #                     self.__game.announce(f"The {attacker} has missed resulting in {0} damage to {defender} hp."
    #                                          f"The {defender} has {defender.get_current_hp()} hp.")
    #             else:
    #                 self.__game.announce(f"The {attacker} has missed resulting in {0} damage to {defender} hp."
    #                                      f"The {defender} has {defender.get_current_hp()} hp.")
    #
    #     if attacker.get_current_hp() <= 0:
    #         self.__game.announce(
    #             f"The {attacker} hp is {attacker.get_current_hp()}/{attacker.get_generated_hp}. You have died.")
    #         attacker.is_dead()
    #     elif defender.get_current_hp() <= 0:
    #         self.__game.announce(
    #             f"The {defender} hp is {defender.get_current_hp()}/{defender.get_generated_hp}. The {defender}"
    #             f" has died.")

    # @abstractmethod
    def __str__(self):
        """
        Returns a string representation of the Dungeon Character.
        """

        # produce a content line for each status item
        name_str = f"Name: {self.__name}"
        hp_str = f"HP: {self.__current_hp} / {self.__generated_hp}"
        attack_str = f"Attack Range: {self.__attack_min} to {self.__attack_max}"
        speed_str = f"Speed: {self.__attack_speed}"
        dodge_str = f"Dodge Chance: {round(self.__chance_to_dodge_min * 100)}% to {round(self.__chance_to_dodge_max * 100)}% "
        accuracy_str = f"Hit Chance: {round(self.__chance_to_hit_min * 100)}% to {round(self.__chance_to_hit_max * 100)}%"

        return [name_str, hp_str, attack_str, speed_str, dodge_str, accuracy_str]

# kevin = DungeonCharacter("Kevin", Game(), 200, 300, 40, 80, 4, .70, .85, .30, .40)
# talia = DungeonCharacter("Talia", Game(), 100, 200, 30, 80, 3, .30, .65, .20, .30)
# kevin.fight(kevin, talia)


# print(kevin)
# print(talia)

# DungeonCharacter.combat(kevin, talia)



# CombatMode()
