import random
from warrior import Warrior
from cleric import Cleric
from thief import Thief
from phonenix import Phoenix



class CombatMode():
    def combat(self, attacker, defender):

        while defender.get_current_hp() > 0 and attacker.get_current_hp() > 0:

            dodge_chance = random.uniform(.1, 1)
            # character will attack another character
            hit_chance = random.uniform(.1, 1)  # generates a random % chance of a successful attack by this character
            if attacker.get_attack_speed >= defender.get_attack_speed:

                if attacker.get_chance_to_hit >= hit_chance:
                    if defender.get_chance_to_dodge < dodge_chance:
                        attacker.get_attack_damage_range() - defender.get_current_hp()
                        print(
                            f"The {attacker} has dealt the {defender} {attacker.get_damage_range()} damage to their hp."
                            f"The {defender} has {defender.get_current_hp()} hp.")
                    else:
                        print(f"The {attacker} has missed resulting in {0} damage to {defender} hp."
                              f"The {defender} has {defender.get_current_hp()} hp.")
                else:
                    print(f"The {attacker} has missed resulting in {0} damage to {defender} hp."
                          f"The {defender} has {defender.get_current_hp()} hp.")

            elif attacker.get_attack_speed < defender.get_attack_speed:
                if defender.get_chance_to_hit >= hit_chance:
                    if attacker.get_chance_to_dodge < dodge_chance:
                        defender.get_attack_damage_range() - attacker.get_current_hp()
                        print(f"The {defender} has dealt the {attacker} {defender.get_damage_range()} damage to"
                              f" their hp. The {attacker} has {attacker.get_current_hp()} hp.")
                    else:
                        print(f"The {defender} has missed resulting in {0} damage to {attacker} hp."
                              f"The {attacker} has {attacker.get_current_hp()} hp.")
                else:
                    print(f"The {defender} has missed resulting in {0} damage to {attacker} hp."
                          f"The {attacker} has {attacker.get_current_hp()} hp.")

            if attacker.get_current_hp() <= 0:
                print(
                    f"The {attacker} hp is {attacker.get_current_hp()}/{attacker.get_generated_hp}. You have died.")
                attacker.is_dead()
            elif defender.get_current_hp() <= 0:
                print(
                    f"The {defender} hp is {defender.get_current_hp()}/{defender.get_generated_hp}. The {defender}"
                    f" has died.")


    # def combat(self, attacker, defender):
    #     while defender.hp > 0 or attacker.hp > 0:
    #         attack = int(random.random() * attacker.attack)
    #         defense = int(random.random() * defender.defense)
    #         print("Attack: %s vs Defense: %s" % (str(attack), str(defense)))
    #         if attacker.get_speed >= defense.get_speed:
    #             print("You hit the %s for %s HP." % (defender.name.capitalize(), str(attack)))
    #             defender.hp -= attack
    #         elif attack == defense:
    #             print
    #             "The attack missed. You feel kind of disappointed."
    #         else:
    #             print("The %s hit you for %s HP and it hurt real bad.") % (defender.name.capitalize(), str(attack))
    #             self.hero.hp -= attack
    #     if defender.hp <= 0:
    #         print(
    #         "You killed the %s. How sad for the %s's family." % (defender.name.capitalize(), defender.name.capitalize()))
    #         del self.current_room.monster_list[defender.name]
    #     if self.hero.hp < 1:
    #         self.hero.death()


