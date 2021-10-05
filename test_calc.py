import unittest
from calc import Calculator as cl


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(cl.add(cl ,10, 5), 15)
        self.assertEqual(cl.add(cl ,-1, 1), 0)
        self.assertEqual(cl.add(cl ,-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(cl.subtract(cl ,10, 5), 5)
        self.assertEqual(cl.subtract(cl ,-1, 1), -2)
        self.assertEqual(cl.subtract(cl ,-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(cl.multiply(cl ,10, 5), 50)
        self.assertEqual(cl.multiply(cl ,-1, 1), -1)
        self.assertEqual(cl.multiply(cl ,-1, -1), 1)

    def test_divide(self):
        self.assertEqual(cl.divide(cl ,10, 5), 2)
        self.assertEqual(cl.divide(cl ,-1, 1), -1)
        self.assertEqual(cl.divide(cl ,-1, -1), 1)
        self.assertEqual(cl.divide(cl ,5, 2), 2.5)

    def test_zero_dev(self):
        self.assertRaises(ValueError, cl.divide, self, x=10, y=0)


if __name__ == '__main__':
    unittest.main()
