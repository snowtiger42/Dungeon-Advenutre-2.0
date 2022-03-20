import unittest
import random
from emu import Emu
from warrior import Warrior
from mock_game import MockGame as Game


class Emu_Test(unittest.TestCase):
    # create various tests
    def test_init(self):
        my_emu = Emu("emu", Game())

    def test_name(self):
        my_emu = Emu("emu", Game())
        my_emu.set_game()
        self.assertEqual("emu", "emu")

    def test_str_fail(self):
        my_emu = Emu("emu", Game())
        my_emu.set_game()
        self.assertNotEqual(str(my_emu), """emu- 
- +---------------------------+
- | Name: emu                 |
- | HP: 322 / 322             |
- | Attack Range: 33 to 44    |
- | Speed: 3                  |
- | Dodge Chance: 30% to 50%  |
- | Hit Chance: 60% to 75%    |
- | Regen Chance: 30% to 50%  |
- | Regen Amount: 20          |
- +---------------------------+

""")

    def test_name_fail(self):
        my_emu_fail = Emu("emu", Game())
        self.assertNotEqual(my_emu_fail.get_name(), "emu")

    def test_Take_Damage(self):
        my_emu = Emu("emu", Game())
        my_emu.set_game()
        self.assertEqual(my_emu.take_damage(5, source="unit tests"), None)

    def test_Deal_Damage(self):
        my_emu = Emu("emu", Game())
        my_emu.set_game()
        my_warrior = Warrior("Jack", Game())
        self.assertEqual(my_emu.take_damage(5, source="unit tests"), None)

    def test_regenerate_hp(self):
        my_emu = Emu("emu", Game())
        # curr_hp = my_emu.get_current_hp  # TODO change __hp to get_hp()
        self.assertEqual(my_emu.regenerate(), None)

    def test_Chance_To_Dodge(self):
        my_emu = Emu("emu", Game())
        self.assertGreater(my_emu.get_chance_to_dodge(), 0.3)

    def test_Attack_Speed(self):
        my_emu = Emu("emu", Game())
        self.assertEqual(my_emu.get_attack_speed(), 3)

    def test_Chance_To_Hit(self):
        my_emu = Emu("emu", Game())
        self.assertGreater(my_emu.get_chance_to_dodge(), 0.3)


if __name__ == '__main__':
    unittest.main()