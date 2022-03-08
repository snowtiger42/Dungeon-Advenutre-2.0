import shelve


class LoadGame:
    def __init__(self):
        pass

    def load_slot_1(self):
        load_slot_1 = shelve.open('save_slot_1')
        load_slot_1.close()

    def load_slot_2(self):
        load_slot_2 = shelve.open('save_slot_2')
        load_slot_2.close()

    def load_slot_3(self):
        load_slot_3 = shelve.open('save_slot_3')
        load_slot_3.close()
