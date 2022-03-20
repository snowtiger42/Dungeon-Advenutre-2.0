import unittest
import random
from sphinx import Sphinx
from warrior import Warrior
from mock_game import MockGame as Game


class Sphinx_Test(unittest.TestCase):
    # create various tests
    def test_init(self):
        my_sphinx = Sphinx("sphinx", Game())

    def test_name(self):
        my_sphinx = Sphinx("sphinx", Game())
        my_sphinx.set_game()
        self.assertEqual("sphinx", "sphinx")

    def test_str_fail(self):
        my_sphinx = Sphinx("sphinx", Game())
        my_sphinx.set_game()
        self.assertNotEqual(str(my_sphinx), """sphinx- 
- +---------------------------+
- | Name: sphinx              |
- | HP: 274 / 274             |
- | Attack Range: 40 to 60    |
- | Speed: 1                  |
- | Dodge Chance: 10% to 25%  |
- | Hit Chance: 40% to 60%    |
- | Regen Chance: 10% to 20%  |
- | Regen Amount: 20          |
- +---------------------------+""")

    def test_name_fail(self):
        my_sphinx_fail = Sphinx("sphinx", Game())
        self.assertNotEqual(my_sphinx_fail.get_name(), "emu")

    def test_Take_Damage(self):
        my_sphinx = Sphinx("sphinx", Game())
        my_sphinx.set_game()
        self.assertEqual(my_sphinx.take_damage(5, source="unit tests"), None)

    def test_Deal_Damage(self):
        my_sphinx = Sphinx("Sphick", Game())
        my_warrior = Warrior("Jack", Game())
        my_sphinx.set_game()
        self.assertEqual(my_sphinx.take_damage(5, source="unit tests"), None)

    def test_regenerate_hp(self):
        my_sphinx = Sphinx("sphinx", Game())
        self.assertEqual(my_sphinx.regenerate(), None)

    def test_Chance_To_Dodge(self):
        my_sphinx = Sphinx("sphinx", Game())
        self.assertGreater(my_sphinx.get_chance_to_dodge(), 0.1)

    def test_Attack_Speed(self):
        my_sphinx = Sphinx("sphinx", Game())
        self.assertEqual(my_sphinx.get_attack_speed(), 1)

    def test_Chance_To_Hit(self):
        my_sphinx = Sphinx("sphinx", Game())
        self.assertGreater(my_sphinx.get_chance_to_dodge(), 0.1)


if __name__ == '__main__':
    unittest.main()