import random
import self as self
# from dungeonCharacter import DungeonCharacter
from mock_game import MockGame as Game
from hero import Hero


class Warrior(Hero):
    """
    A class the handles information for the Warrior
    """

    def __init__(self, name, game):
        super().__init__(name, game, 150, 200, 30, 80, 4, .60, .75, .3, .4, .30, .5)
        # self.__name = name
        # self.__game = game

    def special_move(self):
        if self.get_current_hp() <= 0:
            self.is_dead()
        reduced_chance_to_hit = (self.get_chance_to_hit()) / 2
        hitChance = random.uniform(.1, 1)
        damage = (self.get_attack_damage_range()) * 3

        if reduced_chance_to_hit >= hitChance:
            new_hp = self.get_current_hp()
            result = new_hp - damage

            if result <= self.get_generated_hp():
                self.set_current_hp(0)
            else:
                self.set_current_hp(result)
            self.__game.announce(f"You used the Crushing Blow ability! It deals {damage} damage, bringing your opponent's HP to "
                  f"{self.get_current_hp()}.")
            return True
        else:
            self.__game.announce(f"You used the Crushing Blow ability and Missed! It deals {0} damage, bringing your opponent's HP to "
                  f"{self.get_current_hp()}.")
            return False

# adventurer = Warrior("Pranav", Game())
# # me = Warrior("Kevin")
# print(adventurer)
# print("my name is ", adventurer.get_name())
# print(me)
#
# me.special_move()
# me.special_move()
# me.special_move()
# me.special_move()
# me.special_move()
# print(me)


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
#
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
