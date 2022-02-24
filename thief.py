import random
import self as self
from dungeonCharacter import DungeonCharacter
from mock_game import MockGame as Game
from hero import Hero


class Thief(Hero):
    """
    A class the handles information for the Thief
    """
    def __init__(self, name):
        super().__init__(name, 100, 150, 30, 50, 7, .80,
                         .90, random.uniform(.80, .90), .5, .6, random.uniform(.5, .6), .2, .25,
                         random.uniform(.2, .25))
        self.__name = name

    def special_move(self):
        # hitChance = DungeonCharacter.get_chance_to_hit(self) // 2
        # damage = (DungeonCharacter.get_attack_damage_range(self)) * 3
        #
        # if hitChance >= 1:
        #     hp = DungeonCharacter.get_current_hp(self)
        #     hp -= damage
        pass


thief = Thief("Kevin")
print(thief)


