import unittest
from calc import Calculator as cl


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cl.add(10, 5), 15)
        self.assertEqual(cl.add(-1, 1), 0)
        self.assertEqual(cl.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(cl.subtract(10, 5), 5)
        self.assertEqual(cl.subtract(-1, 1), -2)
        self.assertEqual(cl.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(cl.multiply(10, 5), 50)
        self.assertEqual(cl.multiply(-1, 1), -1)
        self.assertEqual(cl.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(cl.divide(10, 5), 2)
        self.assertEqual(cl.divide(-1, 1), -1)
        self.assertEqual(cl.divide(-1, -1), 1)
        self.assertEqual(cl.divide(5, 0), 2.5)

        with self.assertRaises(ValueError):
            cl.divide(10, 0)


if __name__ == '__main__':
    unittest.main()