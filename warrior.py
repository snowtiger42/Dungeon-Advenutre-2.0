import random
import self as self
from dungeonCharacter import DungeonCharacter
from mock_game import MockGame as Game
from hero import Hero


class Warrior(Hero):
    """
    A class the handles information for the Warrior
    """

    def __init__(self, name):
        super().__init__(name, 100, 200, range(100, 200), range(100, 200), 30, 80, range(30, 80), 4, .60,
                         .75, random.uniform(.60, .75), .3, .5, random.uniform(.3, .5), .30, .5,
                         random.uniform(.3, .5), 0, 0)
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def use_health_potion(self):
        super().use_health_potion()

    # def use_health_potion(self):
    #     Hero.use_health_potion(self)

    def special_move(self):
        hitChance = DungeonCharacter.get_chance_to_hit(self) // 2
        damage = (DungeonCharacter.get_attack_damage_range(self)) * 3

        if hitChance >= 1:
           hp = DungeonCharacter.get_current_hp(self)
           hp -= damage


    # def __str__(self):
    #     prefix = super().__str__()
    #     p = format(prefix)
    #     return print(p)

adventurer = Warrior("Bill")
print(adventurer)


# print("\n------------------------print adventurer status ('empty', try using either potion)-------------------------")
# adventurer.use_health_potion()
# adventurer.use_vision_potion()
#
# print(adventurer)
#
# print("\n------------------------print adventurer status (+1 potion)-------------------------")
# adventurer.add_health_potion()
# print(adventurer)
#
# print("\n------------------------print adventurer status (take damage 1st)-------------------------")
# adventurer.take_damage(1, "angry gnat")
# print(adventurer)

# print("\n------------------------print adventurer status (take 1st health potion)-------------------------")
# adventurer.use_health_potion()
# print(adventurer)
#
#
# print("\n------------------------print adventurer status (Add two of each potion)-------------------------")
# adventurer.add_health_potion()
# adventurer.add_health_potion()
# adventurer.add_vision_potion()
# adventurer.add_vision_potion()
#
# print(adventurer)
#
#
# print("\n------------------------print adventurer status (Add 'A' to the Pillars + adding an extra 'A' and a false 'z')"
#       "-------------------------")
# adventurer.earn_pillar("A")
# try:
#     adventurer.earn_pillar("A")
#     print("should have failed.")
# except:
#     pass
#
# try:
#     adventurer.earn_pillar("z")
#     print("should have failed.")
# except:
#     pass
#
#
# print(adventurer)
#
#
#
# print("\n------------------------print adventurer status (TIME TO DIE!!!)-------------------------")
# print(adventurer)
# adventurer.take_damage(20, "legendary pit")
# adventurer.take_damage(20, "legendary pit")
# adventurer.take_damage(20, "legendary pit")
# adventurer.take_damage(20, "legendary pit")
# adventurer.take_damage(20, "legendary pit")
# adventurer.take_damage(2000, "extra legendary pit")
# print(adventurer)
#
#
#
# print("\n------------------------print adventurer exit (doesn't have all Pillars of OO)-------------------------\n")
# adventurer.exit()
#
# print(adventurer)
#
#
#
# print("\n------------------------print adventurer status (Add 'E', 'I', 'P')-------------------------")
# adventurer.earn_pillar("P")
# adventurer.earn_pillar("I")
# adventurer.earn_pillar("E")
#
# print(adventurer)
#
# print("\n------------------------print adventurer exit (has all Pillars of OO)-------------------------\n")
# adventurer.exit()
