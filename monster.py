from abc import ABCMeta, abstractmethod
from dungeonCharacter import DungeonCharacter
from healAble import HealAble
import random
import base


class Monster(DungeonCharacter, Base):
    __tablename__ = 'monsters'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    room_id = Column(Integer, ForeignKey('rooms.id'))

    def __init__(self, x, y, name, min_hp, max_hp, attack_min, attack_max, attack_speed, chance_to_hit_min, chance_to_hit_max,
                 chance_to_hit, chance_to_dodge_min, chance_to_regenerate_min,
                 chance_to_regenerate_max, regenerate_amount):
        # if self.__class__ == Monster:
        #     raise Exception('I am abstract!')
        super().__init__(x, y, name, min_hp, max_hp, attack_min, attack_max, attack_speed, chance_to_hit_min,
                         chance_to_hit_max, chance_to_hit, chance_to_dodge_min)

        self.__chance_to_regenerate_min = chance_to_regenerate_min
        self.__chance_to_regenerate_max = chance_to_regenerate_max

        self.__chance_to_regenerate = random.uniform(self.__chance_to_regenerate_min, self.__chance_to_regenerate_max)
        self.__regenerate_amount = regenerate_amount

    def get_chance_to_regenerate_min(self):
        return self.__chance_to_regenerate_min

    def set_chance_to_regenerate_min(self, regenerate_min):
        self.__chance_to_regenerate = regenerate_min

    def get_chance_to_regenerate_max(self):
        return self.__chance_to_regenerate_max

    def set_chance_to_regenerate_max(self, regenerate_max):
        self.__chance_to_regenerate_max = regenerate_max

    def get_regenerate_amount(self):
        return self.__regenerate_amount

    def set_regenerate_amount(self, regen_amount):
        self.__regenerate_amount = regen_amount

    def regen_chance_compare(self):
        regen_chance = random.uniform(.1, 1)
        return regen_chance

    def regenerate(self):
        heal = self.__regenerate_amount
        # heal = HealAble().heal()
        current_hp = self.get_current_hp()
        new_hp = current_hp + heal

        if self.get_current_hp() <= 0:
            self.is_dead()

        if self.__chance_to_regenerate >= self.regen_chance_compare():
            self.set_current_hp(new_hp)

            if new_hp >= self.get_generated_hp():
                self.set_current_hp(self.get_generated_hp())
            else:
                self.set_current_hp(new_hp)
            print(f"Managed to regenerate! It heals {heal} HP, bringing it to {self.get_current_hp()}.")
            # self.__game.announce(f"Used a health potion! It heals {heal} HP, bringing you to {self.__current_hp}.")
            return True

        else:
            print(f"Failed to regenerate! It heals {0} HP, bringing it to {self.get_current_hp()}.")
            # self.__game.announce(f"Used a health potion! It heals {heal} HP, bringing you to {self.__current_hp}.")
            return False


    def __str__(self):
        prefix = super().__str__()
        p = format(prefix).replace(',', "" + "\n").replace("('", "").replace("'", " ").replace(")", "     ")
        # p = format(prefix).replace(',', "" + "\n").repslace("('", "").replace("'", " ").replace(")", "     ")

        regen_range_str = f"Regen Chance: {round(self.__chance_to_regenerate_min * 100)}% to " \
                          f"{round(self.__chance_to_regenerate_max * 100)}% "
        regen_amount_str = f"Regen Amount: {self.__regenerate_amount} "

        status_items = [p, regen_range_str, regen_amount_str]
        line_size = 0

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


# c = Monster("Monster", 200, 300, 20, 40, 3, .50, .60, random.uniform(.50, .60), .10, .20, random.uniform(.10, .20),
#             .1, .2, 20)
# print(c)
#
# c.take_damage(100, "Hero")
#
# print(c)
#
# c.regenerate()
#
# print(c)
