import unittest
import random
from emu import Emu
from warrior import Warrior
from mock_game import MockGame as Game


class Emu_Test(unittest.TestCase):
    def test_init(self):
        my_emu = Emu("Ume", Game())

    def test_name(self):
        my_emu = Emu("Ume", Game())
        self.assertEqual(my_emu.get_name(), "Ume")

    def test_str_(self):
        my_emu = Emu("Ume", Game())
        self.assertEqual(str(my_emu), "Ume")

    def test_name_fail(self):
        my_emu_fail = Emu("Umee", Game())
        self.assertNotEqual(my_emu_fail.get_name(), "Ume")

    def test_Take_Damage(self):
        my_emu = Emu("Ume", Game())
        curr_hp = my_emu.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_emu.take_damage(5, source="unit tests"), None)
        self.assertEqual(Emu.__hp, 70)  # TODO change __hp to get_hp()

    def test_Deal_Damage(self):
        my_emu = Emu("Ume", Game())
        my_warrior = Warrior("Jack", Game())
        self.assertEqual(my_emu.deal_damage((5), source="unit tests"), None)
        self.assertEqual(my_warrior.__hp, 15)  # TODO change __hp to get_hp()

    def test_regenerate_hp(self):
        my_emu = Emu("Ume", Game())
        curr_hp = my_emu.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_emu.regenerate_hp(10), None)
        self.assertEqual(my_emu.__hp, curr_hp + 10)  # TODO change __hp to get_hp()

    def test_Chance_To_Dodge(self):
        my_emu = Emu("Ume", Game())
        self.assertEqual(my_emu.chance_to_dodge(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to dodge

    def test_change_to_regenerate(self):
        my_emu = Emu("Ume", Game())
        self.assertEqual(my_emu.chance_to_regenerate(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to regenerate

    def test_Attack_Speed(self):
        my_emu = Emu("Ume", Game())
        self.assertEqual(my_emu.attack_speed(4, source="unit tests"), None)


    def test_Chance_To_Hit(self):
        my_emu = Emu("Ume", Game())
        self.assertEqual(my_emu.chance_to_hit(random.randrange(1, 20), source="unit tests"), None)


if __name__ == '__main__':
    unittest.main()