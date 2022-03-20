import unittest
import random
from raven import Raven
from warrior import Warrior
from mock_game import MockGame as Game


class Raven_test(unittest.TestCase):
    # create various tests
    def test_init(self):
        my_raven = Raven("raven", Game())

    def test_name(self):
        my_raven = Raven("raven", Game())
        my_raven.set_game()
        self.assertEqual("raven", "raven")

    def test_str_fail(self):
        my_raven = Raven("raven", Game())
        self.assertNotEqual(str(my_raven), """emu- 
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
        my_raven_fail = Raven("raven", Game())
        self.assertNotEqual(my_raven_fail.get_name(), "emu")

    def test_Take_Damage(self):
        my_raven = Raven("raven", Game())
        my_raven.set_game()
        self.assertEqual(my_raven.take_damage(5, source="unit tests"), None)

    def test_Deal_Damage(self):
        my_raven = Raven("emu", Game())
        my_raven.set_game()
        my_warrior = Warrior("Jack", Game())
        self.assertEqual(my_raven.take_damage(5, source="unit tests"), None)

    def test_regenerate_hp(self):
        my_raven = Raven("raven", Game())
        self.assertEqual(my_raven.regenerate(), None)

    def test_Chance_To_Dodge(self):
        my_raven = Raven("raven", Game())
        self.assertGreater(my_raven.get_chance_to_dodge(), 0.1)

    def test_Attack_Speed(self):
        my_raven = Raven("raven", Game())
        self.assertEqual(my_raven.get_attack_speed(), 1)

    def test_Chance_To_Hit(self):
        my_raven = Raven("raven", Game())
        self.assertGreater(my_raven.get_chance_to_dodge(), 0.1)


if __name__ == '__main__':
    unittest.main()