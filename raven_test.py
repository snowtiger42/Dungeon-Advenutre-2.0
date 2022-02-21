import unittest
import random
from raven import Raven
from warrior import Warrior
from mock_game import MockGame as Game


class raven_Test(unittest.TestCase):
    def test_init(self):
        my_raven = raven("Ragnar", Game())

    def test_name(self):
        my_raven = raven("Ragnar", Game())
        self.assertEqual(my_not_a_pokemon.get_name(), "Ragnar")

    def test_str_(self):
        my_raven = raven("Ragnar", Game())
        self.assertEqual(str(my_raven), "Ragnar")

    def test_name_fail(self):
        my_raven_fail = raven("Pikachu", Game())
        self.assertNotEqual(my_raven_fail.get_name(), "Ragnar")
        self.assertNotEqual(str(my_raven_fail), "Ragnar")

    def test_Take_Damage(self):
        my_raven = raven("Ragnar", Game())
        curr_hp = my_raven.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_raven.take_damage(5, source="unit tests"), None)
        self.assertEqual(raven.__hp, 70)  # TODO change __hp to get_hp()

    def test_Deal_Damage(self):
        my_raven = raven("Ragnar", Game())
        my_warrior = Warrior("Jack", Game())
        self.assertEqual(raven.deal_damage(5, source="unit tests"), None)
        self.assertEqual(my_warrior.__hp, 15)  # TODO change __hp to get_hp()

    def test_regenerate_hp(self):
        my_raven = raven("Ragnar", Game())
        curr_hp = raven.__hp  # TODO change __hp to get_hp()
        self.assertEqual(my_raven.regenerate_hp(10), None)
        self.assertEqual(my_raven.__hp, curr_hp + 10)  # TODO change __hp to get_hp()

    def test_Chance_To_Dodge(self):
        my_raven = raven("Ragnar", Game())
        self.assertEqual(my_raven.chance_to_dodge(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to dodge

    def test_change_to_regenerate(self):
        my_raven = raven("Ragnar", Game())
        self.assertEqual(my_raven.chance_to_regenerate(random.uniform(.10, .20), source="unit tests"), None)
        # TODO determine proper chance to regenerate

    def test_Attack_Speed(self):
        my_raven = raven("Ragnar", Game())
        self.assertEqual(my_raven.attack_speed(4, source="unit tests"), None)


    def test_Chance_To_Hit(self):
        my_raven = raven("Ragnar", Game())
        self.assertEqual(my_raven.chance_to_hit(random.randrange(1, 20), source="unit tests"), None)


if __name__ == '__main__':
    unittest.main()