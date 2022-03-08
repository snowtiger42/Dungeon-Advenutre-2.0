import random
# import self as self
from dungeonCharacter import DungeonCharacter
from mock_game import MockGame as Game
from hero import Hero


class Thief(Hero):
    """
    A class the handles information for the Thief
    """
    def __init__(self, name, game):
        super().__init__(name, game, 100, 150, 30, 50, 7, .80, .90, .5, .6, .2, .25)
        # self.__name = name

    def special_move(self):
        if self.get_current_hp() <= 0:
            self.is_dead()

        second_chance_to_hit = (self.get_chance_to_hit()) / 2
        hitChance = random.uniform(.1, 1)
        damage = (self.get_attack_damage_range()) * 2

        if second_chance_to_hit >= hitChance:
            new_hp = self.get_current_hp()
            result = new_hp - damage

            if result <= self.get_generated_hp():
                self.set_current_hp(0)
                self.__game.announce(f"You used the Sneak Attack ability, and strike twice! It deals {damage} damage, bringing your "
                      f"opponent's HP to {self.get_current_hp()}.")
            else:
                self.set_current_hp(result)
                self.__game.announce(f"You used the Sneak Attack ability, and strike twice! It deals {damage} damage, bringing your "
                      f"opponent's HP to {self.get_current_hp()}.")
            return True

        elif second_chance_to_hit >= hitChance / 2:
            new_hp = self.get_current_hp()
            result = new_hp - (damage // 2)

            if result >= self.get_generated_hp():
                self.set_current_hp(0)
            else:
                self.set_current_hp(result)
            self.__game.announce(f"You used the Sneak Attack ability, but you were spotted just in time! You strike only once and deal "
                  f"{damage // 2} damage, bringing your "f"opponent's HP to {self.get_current_hp()}.")
        else:
            self.__game.announce(f"You used the Sneak Attack ability and Missed! It deals {0} damage, bringing your opponent's HP to "
                  f"{self.get_current_hp()}.")
            return False


# thief = Thief("Kevin")
# print(thief)
#
# thief.special_move()
# thief.special_move()
# thief.special_move()
# thief.special_move()
# thief.special_move()
# thief.special_move()
# thief.special_move()
#
# print(thief)
#
# thief.add_health_potion()
# thief.use_health_potion()
#
# print(thief)



