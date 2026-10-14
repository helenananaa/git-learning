import unittest
from pricing import final_price


class PricingTests(unittest.TestCase):

    def test_normal_discount(self):
        self.assertEqual(final_price(100, 20), 80)

    def test_no_discount(self):
        self.assertEqual(final_price(50, 0), 50)


if __name__ == "__main__":
    unittest.main()