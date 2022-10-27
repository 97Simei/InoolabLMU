import unittest
from mykaya import my_kaya_equation


class TestMykaya(unittest.TestCase):

    def test_mykaya(self):
        self.assertEqual(my_kaya_equation(
            1, 2, 3, 4), 24, "Should be 24")
        self.assertEqual(my_kaya_equation(
            2, 2, 3, 4), 48, "Should be 48")
        self.assertEqual(my_kaya_equation(
            3, 2, 3, 4), 72, "Should be 72")

    def test__value(self):
        self.assertRaises(ValueError, my_kaya_equation, -1, 2, 3, 4)
        self.assertRaises(ValueError, my_kaya_equation, 1, -2, 3, 4)
        self.assertRaises(ValueError, my_kaya_equation, 1, 2, -3, 4)
        self.assertRaises(ValueError, my_kaya_equation, 1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()
