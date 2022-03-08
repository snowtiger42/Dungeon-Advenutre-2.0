import random
from warrior import Warrior
from cleric import Cleric
from thief import Thief
from phonenix import Phoenix


class CombatMode():
    def combat(self, attacker, defender):
        while defender.hp > 0 and attacker.hp > 0:
            attack = int(random.random() * attacker.attack)
            defense = int(random.random() * defender.defense)
            print("Attack: %s vs Defense: %s" % (str(attack), str(defense)))
            if attack > defense:
                print("You hit the %s for %s HP." % (defender.name.capitalize(), str(attack)))
                defender.hp -= attack
            elif attack == defense:
                print
                "The attack missed. You feel kind of disappointed."
            else:
                print("The %s hit you for %s HP and it hurt real bad.") % (defender.name.capitalize(), str(attack))
                self.hero.hp -= attack
        if defender.hp <= 0:
            print(
                "You killed the %s. How sad for the %s's family." % (
                defender.name.capitalize(), defender.name.capitalize()))
            del self.current_room.monster_list[defender.name]
        if self.hero.hp < 1:
            self.hero.death()
