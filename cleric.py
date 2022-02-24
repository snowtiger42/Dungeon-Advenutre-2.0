import random
from healAble import HealAble
from hero import Hero


class Cleric(Hero):
    """
    A class the handles information for the Cleric
    """

    def __init__(self, name):
        super().__init__(name, 100, 150, 30, 60, 5, .60,
                         .75, random.uniform(.70, .80), .4, .5, random.uniform(.4, .5), .30, .4,
                         random.uniform(.3, .4))
        self.__name = name

    def special_move(self):
        heal = 66
        new_hp = self.get_current_hp() + heal

        if new_hp >= self.get_generated_hp():
            self.set_current_hp(self.get_generated_hp())
        else:
            self.set_current_hp(new_hp)
        print(f"You used the Heal ability! It heals {heal} HP, bringing you to {self.get_current_hp()}.")
        # self.__game.announce(f"Used a health potion! It heals {heal} HP, bringing you to {self.__current_hp}.")
        return True



adventurer = Cleric("Talia")
print(adventurer)


print("\n------------------------print adventurer status ('empty', try using either potion)-------------------------")
adventurer.use_health_potion()
adventurer.use_vision_potion()

adventurer.take_damage(99, "Monster")

print(adventurer)

adventurer.special_move()
adventurer.special_move()
adventurer.special_move()


print(adventurer)


