import unittest

conversion_map = (
    ('X', 10),
    ('IX', 9),
    ('V', 5),
    ('IV', 4),
    ('I', 1))


def ar2rom(val):
    res = ''
    for rom, ar in conversion_map:
        while val >= ar:
            res += rom
            val -= ar
    return res

class Tests(unittest.TestCase):
    def test_1_to_I(self):
        self.assertEqual(ar2rom(1), 'I')

    def test_2_to_II(self):
        self.assertEqual(ar2rom(2), 'II')

    def test_3_to_III(self):
        self.assertEqual(ar2rom(3), 'III')

    def test_4_to_IV(self):
        self.assertEqual(ar2rom(4), 'IV')

    def test_5_to_V(self):
        self.assertEqual(ar2rom(5), 'V')

    def test_9_to_IX(self):
        self.assertEqual(ar2rom(9), 'IX')

    def test_10_to_X(self):
        self.assertEqual(ar2rom(10), 'X')

    def test_20_to_XX(self):
        self.assertEqual(ar2rom(20), 'XX')

    def test_21_to_XXI(self):
        self.assertEqual(ar2rom(21), 'XXI')

if __name__ == "__main__":
    unittest.main()
