from sound_fx import SoundFx
from sound_menu import SoundOption
import tkinter as tk
from tkinter import *
import re
from dungeon_adventure import DungeonAdventure
from load_game import LoadGame


class MainMenu:
    """
    This runs the main menu, through which the user can access the game, read instructions for the game, adjust sound
    options or exit the game.
    """

    def __init__(self):
        """
        Create instance to pass to DungeonAdventure SoundFx instance, player name & difficulty.
        Start menu.
        """
        self.__root = tk.Tk()
        self.__window_size = (1150, 875)
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Dungeon Adventure")
        self.__intro_slide = 0
        self.__start_canvas = None
        self.__dungeon_display = None
        self.__message_log = None
        self.__sound = SoundFx()
        self.__initialize_intro()

    @property
    def sound(self):
        """
        Getter for sound
        :return: obtain user's instance of SoundFx
        :rtype: SoundFx
        """
        return self.__sound

    def __instructions(self):
        """
        Gives the player a briefing on how to play the game.
        """
        instructions = Toplevel(self.__root)
        instructions.title("Instructions")

        button = Button(instructions, font="Verdana 19 bold", text="""Welcome!!! You are about to brave our maze 
        inorder to find the four pillars of OO! Only by collecting these four pillars, will you be able to escape the 
        maze and win the game. In this maze, you will use the 'w' letter to head up, the 'd' letter to go right, 
        the 's' letter to go down and the 'a' letter to go left. Be careful though, for there are pits within the 
        maze that can injure you and if you take to much damage, you will DIE!!! If that happens, the game ends and 
        you'll start over with a new adventurer and a new maze. To help you survive, we have placed some potions 
        within the maze to either restore your HP (health points) by pressing the 'h' button. Or, to help you see 
        deeper within the maze, press the 'j' button. If You wish to check your adventurers stats, press the 'q' button.
        Once you've found all four pillars of OO, find the room with the 0 mark in the maze and enter it to complete the
        maze. Important to note, if the edges have holes, you can walk through them and it'll warp you to the other 
        side of the maze!!!""")
        button.pack()

    def start_loop(self):
        """
        Begins the main loop
        """
        self.__root.mainloop()

    def __initialize_intro(self):
        """
        Sets up canvas for intro slides, then calls the intro method.
        """

        self.__start_canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__start_canvas.configure(bg="#FFBF90")

        self.__start_canvas.pack(expand=True)

        self.__root.bind("<Button-1>", self.__advance_intro)

        self.__advance_intro(None)

    def __advance_intro(self, keypress):
        """
            Each time the method is called, changes the image to create a pseudo-slideshow.
            When the last slide is reached, calls the start menu.
            """
        if self.__intro_slide == 0:
            self.__title_image = tk.PhotoImage(file="assets_intro_1.png")
            self.__start_canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 1:
            self.__title_image = tk.PhotoImage(file="assets_intro_2.png")
            self.__start_canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 2:
            self.__title_image = tk.PhotoImage(file="assets_intro_3.png")
            self.__start_canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 3:
            self.__title_image = tk.PhotoImage(file="assets_controls.png")
            self.__start_canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 4:
            self.__title_image = tk.PhotoImage(file="assets_objectives.png")
            self.__start_canvas.create_image(
                self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER, image=self.__title_image)
            self.__intro_slide += 1
        elif self.__intro_slide == 5:
            self.__start_canvas.destroy()
            self.__root.unbind("<Button-1>")
            self.__start_menu()

    def __start_menu(self):
        """
        Creates and displays the start menu.
        """
        if not self.__start_canvas:
            self.__start_canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
            self.__start_canvas.pack(expand=True)

            self.__title_image = tk.PhotoImage(file="title.png")
            self.__start_canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                             image=self.__title_image)
        else:
            self.__reset_start_canvas("assets_title.png")

        # --Buttons
        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        st_menu_button1 = tk.Button(text='Start', font="Verdana 10 bold", width=5)
        self.__start_canvas.create_window(button_x - 260, button_y, window=st_menu_button1)
        st_menu_button1.config(command=self.__choose_class)

        # st_menu_button1.config(command=self.__input_name)

        st_menu_button2 = tk.Button(text='Instruction', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x, button_y, window=st_menu_button2)
        st_menu_button2.config(command=self.__instructions())

        st_menu_button3 = tk.Button(text='Quit', font="Verdana 10 bold", width=5)
        self.__start_canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
        st_menu_button3.config(command=quit)

        # st_menu_button3 = tk.Button(text='Sound Menu', font="Verdana 10 bold", width=5)
        # self.__start_canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
        # st_menu_button4.config(command=SoundOption.change(self.__sound))
        #
        # st_menu_button3 = tk.Button(text='Load', font="Verdana 10 bold", width=5)
        # self.__start_canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
        # st_menu_button5.config(command=LoadGame())

    def __reset_start_canvas(self, file_str):
        """
            Resets the canvas by deleting it and making a fresh one.
            """
        self.__start_canvas.destroy()
        self.__start_canvas = tk.Canvas(self.__root, width=self.__window_size[0], height=self.__window_size[1])
        self.__start_canvas.configure(bg="#FFBF90")
        self.__start_canvas.pack(expand=True)

        if file_str:
            self.__title_image = tk.PhotoImage(file=file_str)
            self.__start_canvas.create_image(self.__window_size[0] // 2, self.__window_size[1] // 2, anchor=CENTER,
                                             image=self.__title_image)

    def __choose_class(self):
        DA = DungeonAdventure()
        # --Buttons
        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        st_menu_button1 = tk.Button(text='Warrior', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x - 260, button_y, window=st_menu_button1)
        st_menu_button1.config(command=lambda: DA.input_name("warrior"))

        st_menu_button2 = tk.Button(text='Cleric', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x, button_y, window=st_menu_button2)
        st_menu_button2.config(command=lambda: DA.input_name("cleric"))

        st_menu_button3 = tk.Button(text='Thief', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
        st_menu_button3.config(command=lambda: DA.input_name("thief"))
        choose_class = 3

