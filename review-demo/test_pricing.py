import unittest
from pricing import final_price


class PricingTests(unittest.TestCase):

    def test_normal_discount(self):
        self.assertEqual(final_price(100, 20), 80)

    def test_no_discount(self):
        self.assertEqual(final_price(50, 0), 50)

    def test_negative_total(self):
        with self.assertRaises(ValueError):
            final_price(-100, 20)

    def test_excessive_discount(self):
        with self.assertRaises(ValueError):
            final_price(100, 150)

    def test_negative_discount(self):
        with self.assertRaises(ValueError):
            final_price(100, -20)


if __name__ == "__main__":
    unittest.main()