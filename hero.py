import sys
from abc import ABCMeta, abstractmethod
from dungeonCharacter import DungeonCharacter
from mock_game import MockGame as Game
import random


class Hero(DungeonCharacter):
    def __init__(self, chance_to_block_min, chance_to_block_max, chance_to_block, health_p, vision_p):
        # if self.__class__ == Hero:
        #     raise Exception('I am abstract!')
        super(DungeonCharacter, self).__init__()

        self.__chance_to_block_min = chance_to_block_min
        self.__chance_to_block_max = chance_to_block_max
        self.__chance_to_block = chance_to_block
        self.__pillars = []
        self.__vision_p = vision_p
        self.__health_p = health_p
        self.__vision = 0

        # self.__vision_p = 0
        # self.__health_p = 0
        # self.__vision = 0

    def get_health_p(self):
        return self.__health_p

    def set_health_p(self):
        self.__health_p = 0

    def get_vision_p(self):
        return self.__vision_p

    def set_vision_p(self):
        self.__vision_p = 0


    def get_chance_to_block_min(self):
        return self.__chance_to_block_min

    def set_chance_to_block_min(self):
        self.__chance_to_block_min = .30

    def get_chance_to_block_max(self):
        return self.__chance_to_block_max

    def set_chance_to_block_max(self):
        self.__chance_to_block_max = .50

    def get_chance_to_block(self):
        return self.__chance_to_block

    def set_chance_to_block(self):
        self.__chance_to_block = random.uniform(self.__chance_to_block_min, self.__chance_to_block_max)

    @abstractmethod
    def special_move(self):
        pass

    # @abstractmethod
    # def pit_damage(self):
    #     pass
    #
    # @abstractmethod
    # def add_health_potion(self):
    #     pass
    #
    # @abstractmethod
    # def use_health_potion(self):
    #     pass
    #
    # @abstractmethod
    # def add_vision_potion(self):
    #     pass
    #
    # @abstractmethod
    # def use_vision_potion(self):
    #     pass

    def earn_pillar(self, pillar):
        """
        Called by Room to add pillars to Adventurer's inventory.
        """

        if pillar == "A" or pillar == "E" or pillar == "I" or pillar == "P":
            self.__pillars.append(pillar)
            print(f"Earned a pillar!  You now have {self.__pillars}")

            # self.__game.announce(f"Earned a pillar!  You now have {self.__pillars}")

        else:
            raise Exception("The pillar value <" + pillar + "> is neither 'A', 'E', 'I', or 'P'!!!")

    def add_health_potion(self):
        """
        Increments health potion count by 1.
        """
        self.__health_p += 1
        print(f"You pick up a health potion.\nYou now have {self.__health_p} of them.")
        # self.__game.announce(
        #     f"You pick up a health potion.\nYou now have {self.__health_p} of them.")
        return self.__health_p

    def use_health_potion(self):
        """
        If the Adventurer has any health potions, uses one and increases
        Adventurer's health by a random number.
        :returns: True if potion was used, False otherwise
        """
        heal = DungeonCharacter.heal(self)

        if self.__health_p > 0:
            self.__health_p -= 1
            self.__current_hp += heal

            if self.__current_hp >= self.__max_hp:
                self.__current_hp = self.__max_hp

            print(f"Used a health potion! It heals {heal} HP, bringing you to {self.__current_hp}.")
            # self.__game.announce(f"Used a health potion! It heals {heal} HP, bringing you to {self.__current_hp}.")
            return True

        elif self.__health_p <= 0:
            print("You reach for a health potion and find only disappointment.")
            # self.__game.announce("You reach for a health potion and find only disappointment.")
            return False

    def add_vision_potion(self):
        """
        Increments vision potion count by 1.
        """
        self.__vision_p += 1
        print(f"You pick up a vision potion.\nYou now have {self.__vision_p} of them.")
        # self.__game.announce(
        #     f"You pick up a vision potion.\nYou now have {self.__vision_p} of them.")
        return self.__vision_p

    def use_vision_potion(self):
        """
        Uses a vision potion if the Adventurer has one.
        :returns: True if potion used, False otherwise.
        """
        if self.__vision_p > 0:
            self.__vision_p -= 1
            self.__vision += 2
            print(f"Your vision has temporarily increased to {self.__vision}!")

            # self.__game.announce(f"Your vision has temporarily increased to {self.__vision}!")
            return True

        else:
            print("You look for a vision potion but don't see one.")
            # self.__game.announce("You look for a vision potion but don't see one.")
            return False

    def get_vision_range(self):
        """
        Returns vision range of adventurer.
        """
        return self.__vision

    def decay_vision(self):
        """
        Reduces vision by 1 if it's above 0.
        """
        if self.__vision > 0:
            self.__vision -= 1
            print("The effects of your vision potion fade a little.")

            # self.__game.announce("The effects of your vision potion fade a little.")

    # def take_damage(self, damage, source):
    #     """
    #     Reduces HP by the indicated amount and makes an announcement.
    #     """
    #     self.__current_hp -= damage
    #     print(f"Oh no! {self.__name} took {damage} dmg from {source}!\nThey are now at {self.__current_hp} hp!")
    #
    #     # self.__game.announce(f"Oh no! {self.__name} took {damage} dmg from {source}!\nThey are now at {self.__current_hp} hp!")

    def exit(self):
        """
        Ends the game if the adventurer has all four pillars.  Makes an announcement either way.
        """
        if len(self.__pillars) >= 4:
            sys.exit()
            # self.__game.end_game()
            # return
        else:
            print(
                "You feel like you could escape from\nthis room if only you knew more\nabout programming.")
            # self.__game.announce(
            #     "You feel like you could escape from\nthis room if only you knew more\nabout programming.")
            return

    def __str__(self):
        """
        Returns a string representation of the Hero.
        """
        prefix = super().__str__()

        # if prefix is None:
        #     return '{}'.format(prefix)
        # p = format(prefix).replace("['", '').replace(',', "\n").replace("]", " " * 27).replace("'", " |", 10)
        p = format(prefix).replace(',', "" +"\n").replace("('", "").replace("'", " ").replace(")", "     ")

        healthp_str = f"Health potions: {self.__health_p}"
        visionp_str = f"Vision potions: {self.__vision_p}"
        pillar_string = f"Pillars found: {self.__pillars}"
        # super().__str__()

        status_items = [p, healthp_str, visionp_str, pillar_string]
        line_size = 0

        for line in status_items:
            if len(line) > line_size:
                line_size = len(line)

        # create borders
        border = "+" + "-" * (line_size // 5 + 5) + "+"

        # add spacers to all status items based on max length
        # so that right border is even
        output_str = "\n" + border
        for line in status_items:
            output_str += f"\n| {line}"
            white_space = line_size - len(line)
            if white_space > 0:
                output_str += " " * (white_space // 11 + 1)
            output_str += " |"

        output_str += f"\n{border}\n"

        return output_str

    # debug code, only used for unit tests
    def is_pillar_in_inventory(self, pillar):
        return pillar in self.__pillars


# b = Hero(.30, .50, random.uniform(.30, .50))
#
# print(b)
#
# print("\n------------------------print adventurer status ('empty', try using either potion)-------------------------")
# b.use_health_potion()
# b.use_vision_potion()
#
# print(b)
#
# print("\n------------------------print adventurer status (+1 potion)-------------------------")
# b.add_health_potion()
# print(b)
#
# print("\n------------------------print adventurer status (take damage 1st)-------------------------")
# b.take_damage(1, "angry gnat")
# print(b)
#
# print("\n------------------------print adventurer status (take 1st health potion)-------------------------")
# b.use_health_potion()
# print(b)


# print("\n------------------------print adventurer status (Add two of each potion)-------------------------")
# b.add_health_potion()
# b.add_health_potion()
# b.add_vision_potion()
# b.add_vision_potion()
#
# print(b)
#
#
# print("\n------------------------print adventurer status (Add 'A' to the Pillars + adding an extra 'A' and a false 'z')"
#       "-------------------------")
# b.earn_pillar("A")
# try:
#     b.earn_pillar("A")
#     print("should have failed.")
# except:
#     pass
#
# try:
#     b.earn_pillar("z")
#     print("should have failed.")
# except:
#     pass
#
#
# print(b)
#
#
#
# print("\n------------------------print adventurer status (TIME TO DIE!!!)-------------------------")
# print(b)
# b.take_damage(20, "legendary pit")
# b.take_damage(20, "legendary pit")
# b.take_damage(20, "legendary pit")
# b.take_damage(20, "legendary pit")
# b.take_damage(20, "legendary pit")
# b.take_damage(2000, "extra legendary pit")
# print(b)
#
#
#
# print("\n------------------------print adventurer exit (doesn't have all Pillars of OO)-------------------------\n")
# b.exit()
#
# print(b)
#
#
#
# print("\n------------------------print adventurer status (Add 'E', 'I', 'P')-------------------------")
# b.earn_pillar("P")
# b.earn_pillar("I")
# b.earn_pillar("E")
#
# print(b)
#
# print("\n------------------------print adventurer exit (has all Pillars of OO)-------------------------\n")
# b.exit()
