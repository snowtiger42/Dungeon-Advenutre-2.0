import tkinter as tk
from warrior import Warrior
from thief import Thief
from cleric import Cleric
from dungeonCharacter import DungeonCharacter
from hero import Hero

from raven import Raven
from emu import Emu
from sphinx import Sphinx
from phonenix import Phoenix
from mock_game import MockGame as Game

from mockannouncement import MockAnnouncement as Announce

from tkinter import *


class Battleground:
    def __init__(self):
        self.root = tk.Tk()
        self.root.config(bg='#345')
        self.root.title("Combat Mode")
        self.window_size = (1200, 900)
        self.root.geometry(f"{self.window_size[0]}x{self.window_size[1]}+250+100")

    def combat(self, hero, monster):
        self.__hero = hero
        self.__monster = monster

        start_canvas = tk.Canvas(self.root, width=self.window_size[0], height=self.window_size[1])
        start_canvas.configure(bg="#345")
        start_canvas.pack(expand=False)

        tb_y = self.window_size[1] // 2

        # build Hero textbox
        self.__hero_text = tk.Text(start_canvas, width=30, height=15)
        self.__hero_text.place(x=0, y=tb_y, anchor="w")

        self.__hero_text.insert("end", f"         *****Hero Stats*****    {self.__hero}")
        # self.__legend.config(state="disabled") #probably get rid og disabled

        # build Monster textbox
        self.__monster_text = tk.Text(start_canvas, width=30, height=20)
        self.__monster_text.place(x=self.window_size[0], y=tb_y, anchor="e")

        # self.__monster_text.insert("end", f"         *****Monster Stats*****     ")
        self.__monster_text.insert("end", f"         *****Monster Stats*****     {self.__monster}")
        # self.__monster_text.config(state="disabled")

        # build textbox
        self.__message_log = tk.Text(start_canvas, width=60, height=50)
        self.__message_log.place(x=self.window_size[0] // 2, y=tb_y, anchor=CENTER)
        self.__message_log.insert("end", f"            ")

        # self.__message_log.insert("end", f"            ")

        # self.__message_log.config(state="disabled")
        # build dungeon display
        # self.__dungeon_display = tk.Text(self.__start_canvas, width=textbox_size, height=textbox_size)
        # self.__dungeon_display.place(x=self.__window_size[0] // 2, y=tb_y, anchor=CENTER)

        # --Buttons
        button_y = self.window_size[1] / 2 + 240
        button_x = self.window_size[0] / 2 - 40

        bt_menu_button1 = tk.Button(self.root, text='Fight', font="Verdana 10 bold", width=12)
        start_canvas.create_window(button_x - 450, button_y - 50, window=bt_menu_button1)
        # self.__start_canvas.create_window(button_x, button_y - 400, window=st_menu_button1)
        bt_menu_button1.config(command=lambda: self.combat_commands(self.__hero, self.__monster, "Fight"))


        bt_menu_button2 = tk.Button(self.root, text='Special Move', font="Verdana 10 bold", width=12)
        start_canvas.create_window(button_x - 450, button_y, window=bt_menu_button2)
        # self.__start_canvas.create_window(button_x, button_y - 250, window=st_menu_button2)
        bt_menu_button2.config(command=lambda: self.combat_commands(self.__hero, self.__monster, "Special Move"))
        # st_menu_button2.config(command=lambda: self.__input_name("cleric"))


        bt_menu_button3 = tk.Button(self.root, text='Use Potion', font="Verdana 10 bold", width=12)
        start_canvas.create_window(button_x - 450, button_y + 50, window=bt_menu_button3)
        # self.__start_canvas.create_window(button_x, button_y - 100, window=st_menu_button3)
        bt_menu_button3.config(command=lambda: self.combat_commands(self.__hero, self.__monster, "Potion"))
        # st_menu_button3.config(command=lambda: self.test_damage("monster"))

    def combat_commands(self, hero, monster, choice):
        # if hero.get_current_hp() <= 0 or monster.get_current_hp() <= 0:
        #     self.root.destroy()

        if choice == "Fight":
            hero.fight(hero, monster)
            # hero.fight(hero, monster)

            # monster.fight(monster, hero)
            if hero.get_current_hp() <= 0 or monster.get_current_hp() <= 0:
                self.root.destroy()

        elif choice == "Special Move":
            if hero == Cleric(Game, hero.get_name()):
                hero.special_move(hero)
                hero.fight(hero, monster)
            else:
                hero.special_move(monster)
                hero.fight(hero, monster)

            # monster.fight(monster, hero)
            if hero.get_current_hp() <= 0 or monster.get_current_hp() <= 0:
                self.root.destroy()

        elif choice == "Potion":
            hero.use_health_potion()
            hero.fight(hero, monster)

            # monster.fight(monster, hero)
            if hero.get_current_hp() <= 0 or monster.get_current_hp() <= 0:
                self.root.destroy()


    def announce(self, message): #change battle log back to announce if no sucess (be sure to fix all classes that changed to self.__announce_battle_log)
        """
        Given a string, prints it to the message log
        """

        log_text = self.__message_log.get("1.0", "end")
        log_text += message
        log_text = log_text.split("\n")

        # log_length = self.window_size.get_size()
        #
        # if len(log_text) > log_length:
        #     log_text = log_text[-log_length:]

        log_text = "\n".join(log_text)

        self.__message_log.config(state="normal")
        self.__message_log.delete("1.0", "end")
        self.__message_log.insert("end", log_text)
        # self.__message_log.config(state="disabled") #"enable this"

    def announce_hero_stats(self, message):
        """
        Given a string, prints it to the message log
        """

        log_text = self.__hero_text.get("1.0", "end")
        log_text += message
        log_text = log_text.split("\n")

        log_length = self.window_size.get_size()

        # log_length = self.__dungeon.get_size() * 3 - 5

        if len(log_text) > log_length:
            log_text = log_text[-log_length:]

        log_text = "\n".join(log_text)

        self.__hero_text.config(state="normal")
        self.__hero_text.delete("1.0", "end")
        self.__hero_text.insert("end", log_text)
        self.__hero_text.config(state="disabled")

    def announce_monster_stats(self, message):
        """
        Given a string, prints it to the message log
        """

        log_text = self.__monster_text.get("1.0", "end")
        log_text += message
        log_text = log_text.split("\n")

        log_length = self.window_size.get_size()
        # log_length = self.__dungeon.get_size() * 3 - 5

        if len(log_text) > log_length:
            log_text = log_text[-log_length:]

        log_text = "\n".join(log_text)

        self.__monster_text.config(state="normal")
        self.__monster_text.delete("1.0", "end")
        self.__monster_text.insert("end", log_text)
        self.__monster_text.config(state="disabled")

    # def announce_battle_log(self, message):
    #     """
    #     Given a string, prints it to the message log
    #     """
    #
    #     log_text = self.__battle_log.get("1.0", "end")
    #     log_text += message
    #     log_text = log_text.split("\n")
    #
    #     log_length = self.window_size.get_size()
    #
    #     if len(log_text) > log_length:
    #         log_text = log_text[-log_length:]
    #
    #     log_text = "\n".join(log_text)
    #
    #     self.__battle_log.config(state="normal")
    #     self.__battle_log.delete("1.0", "end")
    #     self.__battle_log.insert("end", log_text)
    #     self.__battle_log.config(state="disabled")

        tk.mainloop()


