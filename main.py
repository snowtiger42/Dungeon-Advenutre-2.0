from dungeon_adventure import DungeonAdventure as DA
from main_menu import Instructions


class Main:
    def __init__(self):
        Instructions()
        new_adventure = DA()
        new_adventure.start_loop()


if __name__ == '__main__':
    Main()
