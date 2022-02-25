from array import array
import binary
import linear
import unittest

class SearchTest(unittest.TestCase):
    a = [1,6,7,9,10,15]
    def test_binary(self):
        self.assertEqual(binary.binary_search(self.a, 0, len(self.a)-1, 9), 3)
        self.assertEqual(binary.binary_search(self.a, 0, len(self.a)-1, 6), 1)
        self.assertEqual(binary.binary_search(self.a, 0, len(self.a)-1, 20), -1)

    def test_linear(self):
        self.assertEqual(linear.linear_search(self.a, 9), 3)
        self.assertEqual(linear.linear_search(self.a, 6), 1)
        self.assertEqual(linear.linear_search(self.a, 20), -1)


if __name__ == '__main__':
    unittest.main()