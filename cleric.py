import random
from healAble import HealAble
from hero import Hero


class Cleric(Hero):
    """
    A class the handles information for the Cleric
    """

    def __init__(self, name, game):
        super().__init__(name, game, 100, 175, 30, 60, 5, .75, .80, .4, .5, .30, .4)
        # self.__name = name

    def special_move(self):
        reduced_chance_to_hit = (self.get_chance_to_hit()) / 2
        hitChance = random.uniform(.1, 1)
        heal = 66
        new_hp = self.get_current_hp() + heal

        if reduced_chance_to_hit >= hitChance:
            if new_hp >= self.get_generated_hp():
                self.set_current_hp(self.get_generated_hp())
            else:
                self.set_current_hp(new_hp)
            self.__game.announce(f"You used the Heal ability! It heals {heal} HP, bringing you to {self.get_current_hp()}.")
            # self.__game.announce(f"Used a health potion! It heals {heal} HP, bringing you to {self.__current_hp}.")
            return True
        else:
            self.__game.announce(f"You tried to used the Heal ability, but it failed to work! It heals {0} HP, bringing you to "
                  f"{self.get_current_hp()}.")
            return False


# adventurer = Cleric("Talia")
# print(adventurer)
#
#
# print("\n------------------------print adventurer status ('empty', try using either potion)-------------------------")
# adventurer.use_health_potion()
# adventurer.use_vision_potion()
#
# adventurer.take_damage(99, "Phoenix")
#
# print(adventurer)
#
# adventurer.special_move()
# adventurer.special_move()
# adventurer.special_move()
#
#
# print(adventurer)


