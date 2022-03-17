# import random
# from warrior import Warrior
# from cleric import Cleric
# from thief import Thief
# from phonenix import Phoenix
# # from dungeon import Dungeon
# from tkinter import *
# import tkinter as tk
# # from dungeon_adventure import DungeonAdventure as DA
#
#
# class CombatMode():
#
#
#     def __init__(self):
#         self.__start_canvas = None
#         self.__window_size = (1150, 875)
#         self.__root = tk.Tk()
#         self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
#
#         # self.__hero = DA.self.__hero
#
#     top = tkinter.Tk()
#
#     C = tkinter.Canvas(top, bg="blue", height=250, width=300)
#
#     coord = 10, 50, 240, 210
#     arc = C.create_arc(coord, start=0, extent=150, fill="red")
#
#     C.pack()
#     top.mainloop()
#     def __reset_start_canvas(self, file_str):
#         """
#         Resets the canvas by deleting it and making a fresh one.
#         """
#         self.__start_canvas.destroy()
#         self.__start_canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
#         self.__start_canvas.configure(bg="#FFBF90")
#         self.__start_canvas.pack(expand=True)
#
#
#     def combat(self):
#         self.__reset_start_canvas(None)
#         # DA.self.__reset_start_canvas(None)
#         # Setup dungeon & get size
#         # self.__dungeon = Dungeon(self.__diff, self, self.__hero)
#         textbox_size = self.__window_size.get_size() * 3
#         tb_y = self.__window_size[1] // 2
#
#         # build legend textbox
#         self.__legend = tk.Text(self.__start_canvas, width=38, height=textbox_size)
#         self.__legend.place(x=0, y=tb_y, anchor="w")
#
#         spacer = "\n" * ((textbox_size - 10) // 2)
#         self.__legend.insert("end", spacer + f"           *****Hero Stats***** \n\n   ")
#         self.__legend.config(state="disabled") #probably get rid og disabled
#
#
#     # def combat(self, attacker, defender):
#     #
#     #     while defender.get_current_hp() > 0 and attacker.get_current_hp() > 0:
#     #
#     #         dodge_chance = random.uniform(.1, 1)
#     #         # character will attack another character
#     #         hit_chance = random.uniform(.1, 1)  # generates a random % chance of a successful attack by this character
#     #         if attacker.get_attack_speed >= defender.get_attack_speed:
#     #
#     #             if attacker.get_chance_to_hit >= hit_chance:
#     #                 if defender.get_chance_to_dodge < dodge_chance:
#     #                     attacker.get_attack_damage_range() - defender.get_current_hp()
#     #                     print(
#     #                         f"The {attacker} has dealt the {defender} {attacker.get_damage_range()} damage to their hp."
#     #                         f"The {defender} has {defender.get_current_hp()} hp.")
#     #                 else:
#     #                     print(f"The {attacker} has missed resulting in {0} damage to {defender} hp."
#     #                           f"The {defender} has {defender.get_current_hp()} hp.")
#     #             else:
#     #                 print(f"The {attacker} has missed resulting in {0} damage to {defender} hp."
#     #                       f"The {defender} has {defender.get_current_hp()} hp.")
#     #
#     #         elif attacker.get_attack_speed < defender.get_attack_speed:
#     #             if defender.get_chance_to_hit >= hit_chance:
#     #                 if attacker.get_chance_to_dodge < dodge_chance:
#     #                     defender.get_attack_damage_range() - attacker.get_current_hp()
#     #                     print(f"The {defender} has dealt the {attacker} {defender.get_damage_range()} damage to"
#     #                           f" their hp. The {attacker} has {attacker.get_current_hp()} hp.")
#     #                 else:
#     #                     print(f"The {defender} has missed resulting in {0} damage to {attacker} hp."
#     #                           f"The {attacker} has {attacker.get_current_hp()} hp.")
#     #             else:
#     #                 print(f"The {defender} has missed resulting in {0} damage to {attacker} hp."
#     #                       f"The {attacker} has {attacker.get_current_hp()} hp.")
#     #
#     #         if attacker.get_current_hp() <= 0:
#     #             print(
#     #                 f"The {attacker} hp is {attacker.get_current_hp()}/{attacker.get_generated_hp}. You have died.")
#     #             attacker.is_dead()
#     #         elif defender.get_current_hp() <= 0:
#     #             print(
#     #                 f"The {defender} hp is {defender.get_current_hp()}/{defender.get_generated_hp}. The {defender}"
#     #                 f" has died.")
#
#
#     # def combat(self, attacker, defender):
#     #     while defender.hp > 0 or attacker.hp > 0:
#     #         attack = int(random.random() * attacker.attack)
#     #         defense = int(random.random() * defender.defense)
#     #         print("Attack: %s vs Defense: %s" % (str(attack), str(defense)))
#     #         if attacker.get_speed >= defense.get_speed:
#     #             print("You hit the %s for %s HP." % (defender.name.capitalize(), str(attack)))
#     #             defender.hp -= attack
#     #         elif attack == defense:
#     #             print
#     #             "The attack missed. You feel kind of disappointed."
#     #         else:
#     #             print("The %s hit you for %s HP and it hurt real bad.") % (defender.name.capitalize(), str(attack))
#     #             self.hero.hp -= attack
#     #     if defender.hp <= 0:
#     #         print(
#     #         "You killed the %s. How sad for the %s's family." % (defender.name.capitalize(), defender.name.capitalize()))
#     #         del self.current_room.monster_list[defender.name]
#     #     if self.hero.hp < 1:
#     #         self.hero.death()
#
#
