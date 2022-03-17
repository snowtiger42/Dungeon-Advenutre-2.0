import unittest
import random
from sphinx import Sphinx
from warrior import Warrior
from mock_game import MockGame as Game


class Sphinx_Test(unittest.TestCase):
    def test_init(self):
        my_sphinx = Sphinx("Sphick", Game())

    def test_name(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertEqual(my_sphinx.get_name(), "Sphick")

    def test_str_(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertEqual(str(my_sphinx), "Sphick")

    def test_name_fail(self):
        my_sphinx_fail = Sphinx("Sphicholas", Game())
        self.assertNotEqual(my_sphinx_fail.get_name(), "Sphick")
        self.assertNotEqual(str(my_sphinx_fail), "Sphick")

    def test_Take_Damage(self):
        my_sphinx = Sphinx("Sphick", Game())
        curr_hp = my_sphinx.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_sphinx.take_damage(5, source="unit tests"), None)
        self.assertEqual(Sphinx.__hp, 70)  # TODO change __hp to get_hp()

    def test_Deal_Damage(self):
        my_sphinx = Sphinx("Sphick", Game())
        my_warrior = Warrior("Jack", Game())
        self.assertEqual(my_sphinx.deal_damage(5, source="unit tests"), None)
        self.assertEqual(my_warrior.__hp, 15)  # TODO change __hp to get_hp()

    def test_regenerate_hp(self):
        my_sphinx = Sphinx("Sphick", Game())
        curr_hp = my_sphinx.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_sphinx.regenerate_hp(10), None)
        self.assertEqual(my_sphinx.__hp, curr_hp + 10)  # TODO change __hp to get_hp()

    def test_Chance_To_Dodge(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertEqual(my_sphinx.chance_to_dodge(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to dodge

    def test_change_to_regenerate(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertEqual(my_sphinx.chance_to_regenerate(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to regenerate

    def test_Attack_Speed(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertEqual(my_sphinx.attack_speed(4, source="unit tests"), None)


    def test_Chance_To_Hit(self):
        my_sphinx = Sphinx("Sphick", Game())
        self.assertEqual(my_sphinx.chance_to_hit(random.randrange(1, 20), source="unit tests"), None)


if __name__ == '__main__':
    unittest.main()