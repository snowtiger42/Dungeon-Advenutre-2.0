from abc import ABCMeta, abstractmethod
from dungeonCharacter import DungeonCharacter
import random


class Monster(DungeonCharacter):
    def __init__(self, name, min_hp, max_hp, generated_hp, current_hp, attack_min, attack_max, attack_damage_range,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_hit, chance_to_dodge_min,
                 chance_to_dodge_max, chance_to_dodge, chance_to_regenerate_min, chance_to_regenerate_max,
                 regenerate_amount):
        # if self.__class__ == Monster:
        #     raise Exception('I am abstract!')
        super().__init__(name, min_hp, max_hp, generated_hp, current_hp, attack_min, attack_max, attack_damage_range,
                         attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_hit, chance_to_dodge_min,
                         chance_to_dodge_max, chance_to_dodge)

        self.__chance_to_regenerate_min = chance_to_regenerate_min
        self.__chance_to_regenerate_max = chance_to_regenerate_max

        self.__chance_to_regenerate = random.uniform(self.__chance_to_regenerate_min, self.__chance_to_regenerate_max)
        self.__regenerate_amount = regenerate_amount

    def get_chance_to_regenerate_min(self):
        return self.__chance_to_regenerate_min

    def set_chance_to_regenerate_min(self):
        self.__chance_to_regenerate = .3

    def get_chance_to_regenerate_max(self):
        return self.__chance_to_regenerate_max

    def get_chance_to_regenerate(self):
        self.__chance_to_regenerate_max = .5

    # def get_chance_to_regenerate(self):
    #     return self.__chance_to_regenerate
    #
    # def set_chance_to_regenerate(self):
    #     self.__chance_to_regenerate = random.uniform(self.__chance_to_regenerate_min, self.__chance_to_regenerate_max)

    def get_regenerate_amount(self):
        return self.__regenerate_amount

    def set_regenerate_amount(self):
        self.__regenerate_amount = random.randrange(10, 20)

    def __str__(self):
        prefix = super().__str__()
        p = format(prefix).replace(',', "" + "\n").replace("('", "").replace("'", " ").replace(")", "     ")

        regen_range_str = f"Regen Chance: {round(self.__chance_to_regenerate_min * 100)}% to {round(self.__chance_to_regenerate_max* 100)}% "

        status_items = [p, regen_range_str]
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


# c = Monster(random.uniform(.20, .30), random.randrange(10, 20))
# print(c)
