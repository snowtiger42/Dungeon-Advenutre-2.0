from abc import ABCMeta, abstractmethod
from abc import abstractmethod


<<<<<<< Updated upstream
class DungeonCharacter(metaclass=ABCMeta):
=======
class DungeonCharacter(object, metaclass=ABCMeta):
    # class DungeonCharacter:

    def __init__(self, name, min_hp, max_hp, attack_min, attack_max,
                 attack_speed, chance_to_hit_min, chance_to_hit_max, chance_to_dodge_min,
                 chance_to_dodge_max):
        # don't need generated_hp, current_hp, attack_damage_range
        # chance_to_hit or chance_to_dodge passed in as arguments
        # if self.__class__ == DungeonCharacter:
        #     raise Exception('I am abstract!')
        self.__name = name
        # self.__game = game
        self.__min_hp = min_hp
        self.__max_hp = max_hp

        self.__generated_hp = random.randrange(self.__min_hp, self.__max_hp)
        self.__current_hp = self.__generated_hp  # here it is
        # self.__generated_hp = generated_hp
        # self.__current_hp = current_hp
        self.__attack_min = attack_min
        self.__attack_max = attack_max

        self.__attack_damage_range = random.randrange(self.__attack_min, self.__attack_max)
        # self.__attack_damage_range = attack_damage_range
        self.__attack_speed = attack_speed
        self.__chance_to_dodge_min = chance_to_dodge_min
        self.__chance_to_dodge_max = chance_to_dodge_max
        self.__chance_to_dodge = random.randrange(self.__chance_to_dodge_min, self.__chance_to_dodge_max)
        self.__chance_to_hit_min = chance_to_hit_min
        self.__chance_to_hit_max = chance_to_hit_max
        self.__chance_to_hit = random.randrange(self.__chance_to_hit_min, self.__chance_to_hit_max)

    def get_min_hp(self):
        return self.__min_hp

    def set_min_hp(self):
        self.__min_hp = 100

    def get_max_hp(self):
        return self.__max_hp

    def set_max_hp(self):
        self.__max_hp = 200

    # def get_generated_hp(self):
    #     return self.__generated_hp
    #
    # def set_generated_hp(self):
    #     self.__generated_hp = range(int(self.__min_hp), int(self.__max_hp))
    #
    def get_current_hp(self):
        return self.__current_hp

    def set_current_hp(self):
        self.__current_hp = self.__generated_hp

    def get_attack_min(self):
        return self.__attack_min

    def set_attack_min(self):
        self.__attack_min = 30

    def get_attack_max(self):
        return self.__attack_max

    def set_attack_max(self):
        self.__attack_max = 80

    def get_attack_damage_range(self):
        return self.__attack_damage_range

    def set_attack_damage_range(self):
        self.__attack_damage_range = random.uniform(self.__attack_min, self.__attack_max)

    def get_attack_speed(self):
        return self.__attack_speed

    def set_attack_speed(self, new_speed):
        self.__attack_speed = new_speed

    def get_chance_to_hit_min(self):
        return self.__chance_to_hit_min

    def set_chance_to_hit_min(self, new_hit_min):
        self.__chance_to_hit_min = new_hit_min

    def get_chance_to_hit_max(self):
        return self.__chance_to_hit_max

    def set_chance_to_hit_max(self, new_hit_max):
        self.__chance_to_hit_max = new_hit_max

    def get_chance_to_hit(self):
        return self.__chance_to_hit

    def set_chance_to_hit(self):
        self.__chance_to_hit = random.uniform(self.__chance_to_hit_min, self.__chance_to_hit_max)

    def get_chance_to_dodge_max(self):
        return self.__chance_to_dodge_max

    def set_chance_to_dodge_max(self, new_chance_to_dodge_min):
        self.__chance_to_dodge_max = new_chance_to_dodge_min

    def get_chance_to_dodge_min(self):
        return self.__chance_to_dodge_min

    def set_chance_to_dodge_min(self, new_chance_to_dodge_min):
        self.__chance_to_dodge_min = new_chance_to_dodge_min

    def get_chance_to_dodge(self):
        return self.__chance_to_dodge

    def set_chance_to_dodge(self):
        self.__chance_to_dodge = random.uniform(self.__chance_to_dodge_min, self.__chance_to_dodge_max)


    def heal(self):
        heal = random.randrange(25, 50)

        self.__current_hp += heal

        if self.__current_hp >= self.__generated_hp:
            self.__current_hp = self.__generated_hp

    # @abstractmethod
    # def __str__():
    #     pass
>>>>>>> Stashed changes

    @staticmethod
    @abstractmethod
    def get_name(self):
<<<<<<< Updated upstream
        pass
=======
        """
        Getter for name property.
        """
        return str(self.__name)

    def set_name(self, name):
        self.__name = name

    def is_dead(self):
        """
        Returns true if the adventurer's HP is above 0, and False otherwise.
        """
        return (self.__current_hp <= 0),  # sys.exit()  should we do something before exit?
>>>>>>> Stashed changes

    @staticmethod
    @abstractmethod
    def damage_range(self):
        pass

    @staticmethod
    @abstractmethod
    def attack_speed(self):
        pass

    @staticmethod
    @abstractmethod
    def hit_chance(self):
        pass

    @staticmethod
    @abstractmethod
    def is_dead(self):
        pass


