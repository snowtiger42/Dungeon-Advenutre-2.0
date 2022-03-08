import shelve


class SaveGame:
    def __init__(self):
        pass

    def save_slot_1(self):
        save_slot_1 = shelve.open('save_slot_1')
        save_slot_1.close()

    def save_slot_2(self):
        save_slot_2 = shelve.open('save_slot_2')
        save_slot_2.close()

    def save_slot_3(self):
        save_slot_3 = shelve.open('save_slot_3')
        save_slot_3.close()
