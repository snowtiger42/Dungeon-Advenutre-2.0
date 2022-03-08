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
        self.__DA = DungeonAdventure()
        self.__window_size = (1150, 875)
        self.__root.geometry(f"{self.__window_size[0]}x{self.__window_size[1]}+250+100")
        self.__root.title("Dungeon Adventure")
        self.__intro_slide = 0
        self.__start_canvas = None
        self.__dungeon_display = None
        self.__message_log = None
        self.__sound = SoundFx()
        self.__initialize_intro()
        self.__make_help_menu()

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

        # st_menu_button4 = tk.Button(text='Sound Menu', font="Verdana 10 bold", width=5)
        # self.__start_canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
        # st_menu_button4.config(command=SoundOption.change(self.__sound))
        #
        # st_menu_button5 = tk.Button(text='Load', font="Verdana 10 bold", width=5)
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
        # --Buttons
        button_y = self.__window_size[1] // 2 + 240
        button_x = self.__window_size[0] // 2 - 40

        st_menu_button1 = tk.Button(text='Warrior', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x - 260, button_y, window=st_menu_button1)
        st_menu_button1.config(command=lambda: self.__DA.input_name("warrior"))

        st_menu_button2 = tk.Button(text='Cleric', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x, button_y, window=st_menu_button2)
        st_menu_button2.config(command=lambda: self.__DA.input_name("cleric"))

        st_menu_button3 = tk.Button(text='Thief', font="Verdana 10 bold", width=10)
        self.__start_canvas.create_window(button_x + 260, button_y, window=st_menu_button3)
        st_menu_button3.config(command=lambda: self.__DA.input_name("thief"))
        choose_class = 3

    def __make_help_menu(self):
        """
        Creates the help menu and addes it to application menu.
        """
        # --Menu (Help)
        menu_bar = Menu(self.__root)

        filemenu = Menu(menu_bar, tearoff=0)
        filemenu.add_command(label="New", command=self.__donothing)
        filemenu.add_command(label="Open", command=self.__donothing)
        filemenu.add_command(label="Save", command=self.__donothing)
        filemenu.add_command(label="Save as...", command=self.__donothing)
        filemenu.add_command(label="Close", command=self.__donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.__root.quit)
        menu_bar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menu_bar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.__donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=self.__donothing)
        editmenu.add_command(label="Copy", command=self.__donothing)
        editmenu.add_command(label="Paste", command=self.__donothing)
        editmenu.add_command(label="Delete", command=self.__donothing)
        editmenu.add_command(label="Select All", command=self.__donothing)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Cheats", command=self.__display_cheats)
        help_menu.add_command(label="Dungeon Key", command=self.__dungeon_key_images)
        help_menu.add_command(label="Help request", command=self.__donothing)
        help_menu.add_command(label="Hero Class Info", command=self.__display_class_info)

        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.__root.config(menu=menu_bar)

    def __donothing(self):
        """
        Taunts the player for daring to ask for help.
        """
        filewin = Toplevel(self.__root)
        button = Button(filewin, text="Help yourself fool!!! \n Read a book or something!!!", font="Verdana 20 bold",
                        width=40)
        button.pack()

    def __display_cheats(self):
        """
        Menu option explaining the cheats.
        """
        codes = Toplevel(self.__root)
        button = Button(codes, text="""There are currently seven codes that you can use by typing them on your keyboard 
           (while you are in the maze.) 
           6 = See the whole map (note, this ends as soon as you move) 
           7 = Draw whole map (the whole maze is displayed permanently. (Recommended for people who hate fun)) 
           8 = Increases your health & vision potion count by 50!!! 
           9 = Gives the adventurer all four pillars of OO
           0 = developers hate the player, - 1000 HP. Your Dead
           q = See Adventurer status
           p = Reset the map""", font="Verdana 15 bold",
                        width=90)
        button.pack()

    def __display_class_info(self):
        """
        Taunts the player for daring to ask for help.
        """
        filewin = Toplevel(self.__root)
        button = Button(filewin, text="Hello! You have a choice of Three classes to choose from. \n\n"
                                      "Warrior: The warrior has the highest HP, Attack and chance to block. \nThey also"
                                      " have the lowest speed, accuracy and chance to dodge. \nTheir special move is"
                                      " Crushing Blow and deals three times their \nregular damage, but at the cost of"
                                      "it being half their normal accuracy.\n\n"
                                      "Cleric: The cleric has average HP, Attack, Speed, accuracy and \nchance to "
                                      "dodge/block. Their special move is Heal and will restore a \nset amount of HP.\n"
                                      "\nThief: The thief has the lowest HP, Attack and chance to block. \nHowever."
                                      " they have the highest speed, accuracy and chance to dodge.\nTheir special"
                                      " move is sneak attack and it enables the player to attack twice.\nHowever, it "
                                      "only has a 40% chance of success with another 40% \ndelegated to dealing regular"
                                      " damage. The final 20% has a possibility \nof missing entirely.", justify="left",
                        font="Verdana 20 bold",
                        width=65, height=25)
        button.pack()

    def __dungeon_key_images(self):
        """
        Displays a legend for the dungeon screen.
        """
        dungeon_key = Toplevel(self.__root)
        dungeon_key.title("Dungeon Key")

        button = Button(dungeon_key, text="""Here is the key for images you will find within the dungeon's maze: \n
        @ = The Adventurer
        A = pillar of Abstraction
        E = Pillar of Encapsulation
        I = Pillar of Inheritance
        P = Pillar of Polymorphism
        0 = Exit (Remember that it won't activate until you get all four pillars)
        X = A Pit (removes some HP on enter)
        H = Health Potion (is added into your inventory and removed from room on enter)
        V = Vision Potion (is added into your inventory and removed from room on enter)
        M = Both Potions (is added into your inventory and removed from room on enter)
        " " = Blank Room (nothing to see here move along)
        | = Wall (can't move through this)""", font="Verdana 13 bold", )
        button.pack()
