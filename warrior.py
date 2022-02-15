import random
from hero import Hero


class Warrior(Hero):
    """
    A class the handles information for the Warrior
    """

    def __init__(self):
        super(self.__class__, self).__init__()
        self.__pillars = []
        self.__vision_p = 0
        self.__health_p = 0
        self.__vision = 0

    def get_hp(self):
        self.__max_hp = self.__current_hp
        return self.__max_hp

    def set_hp(self):
        self.__current_hp = random.randrange(150, 200)

    def get_attack_damage_range(self):
        return self.__attack_damage_range

    def set_attack_damage_range(self):
        self.__attack_damage_range = random.randrange(40, 80)

    def get_attack_speed(self):
        return self.__attack_speed

    def set_attack_speed(self):
        self.__attack_speed = 4

    def get_chance_to_hit(self):
        return self.__chance_to_hit

    def set_chance_to_hit(self):
        self.__chance_to_hit = random.uniform(.60, .75)

    def get_chance_to_dodge(self):
        return self.__chance_to_dodge

    def set_chance_to_dodge(self):
        self.__chance_to_dodge = random.uniform(.20, .30)

    def get_chance_to_block(self):
        return self.__chance_to_block

    def set_chance_to_block(self):
        self.__chance_to_block = random.uniform(.30, .50)

    # def pit_damage(self):
    #     pass

    def is_dead(self):
        """
        Returns true if the adventurer's HP is above 0, and False otherwise.
        """
        return self.__current_hp <= 0

    def get_name(self):
        """
        Getter for name property.
        """
        return str(self.__name)

    def earn_pillar(self, pillar):
        """
        Called by Room to add pillars to Adventurer's inventory.
        """

        if pillar == "A" or pillar == "E" or pillar == "I" or pillar == "P":
            self.__pillars.append(pillar)
            self.__game.announce(f"Earned a pillar!  You now have {self.__pillars}")

        else:
            raise Exception("The pillar value <" + pillar + "> is neither 'A', 'E', 'I', or 'P'!!!")

    def add_health_potion(self):
        """
        Increments health potion count by 1.
        """
        self.__health_p += 1
        self.__game.announce(
            f"You pick up a health potion.\nYou now have {self.__health_p} of them.")
        return self.__health_p

    def use_health_potion(self):
        """
        If the Adventurer has any health potions, uses one and increases
        Adventurer's health by a random number.
        :returns: True if potion was used, False otherwise
        """
        heal = random.randrange(25, 50)

        if self.__health_p > 0:
            self.__health_p -= 1

            self.__current_hp += heal
            if self.__current_hp >= self.__max_hp:
                self.__current_hp = self.__max_hp

            self.__game.announce(f"Used a health potion! It heals {heal} HP, bringing you to {self.__current_hp}.")
            return True

        elif self.__health_p <= 0:
            self.__game.announce("You reach for a health potion and find only disappointment.")
            return False

    def add_vision_potion(self):
        """
        Increments vision potion count by 1.
        """
        self.__vision_p += 1
        self.__game.announce(
            f"You pick up a vision potion.\nYou now have {self.__vision_p} of them.")
        return self.__vision_p

    def use_vision_potion(self):
        """
        Uses a vision potion if the Adventurer has one.
        :returns: True if potion used, False otherwise.
        """
        if self.__vision_p > 0:
            self.__vision_p -= 1
            self.__vision += 2
            self.__game.announce(f"Your vision has temporarily increased to {self.__vision}!")
            return True

        else:
            self.__game.announce("You look for a vision potion but don't see one.")
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
            self.__game.announce("The effects of your vision potion fade a little.")

    def take_damage(self, damage, source):
        """
        Reduces HP by the indicated amount and makes an announcement.
        """
        self.__current_hp -= damage
        self.__game.announce(f"Oh no! {self.__name} took {damage} dmg from {source}!\nThey are now at {self.__current_hp} hp!")

    def exit(self):
        """
        Ends the game if the adventurer has all four pillars.  Makes an announcement either way.
        """
        if len(self.__pillars) >= 4:
            self.__game.end_game()
            return
        else:
            self.__game.announce(
                "You feel like you could escape from\nthis room if only you knew more\nabout programming.")
            return

    def __str__(self):
        """
        Returns a string representation of the Adventurer.
        """

        # produce a content line for each status item
        name_str = f"Name: {self.__name}"
        hp_str = f"HP: {self.__current_hp} / {self.__max_hp}"
        healthp_str = f"Health potions: {self.__health_p}"
        visionp_str = f"Vision potions: {self.__vision_p}"
        pillar_string = f"Pillars found: {self.__pillars}"

        status_items = [name_str, hp_str, healthp_str, visionp_str, pillar_string]

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

    # debug code, only used for unit tests
    def is_pillar_in_inventory(self, pillar):
        return pillar in self.__pillars
