import unittest

conversion_map = (
    ('x', 10),
    ('ix', 9),
    ('v', 5),
    ('iv', 4),
    ('i', 1))


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

<<<<<<< 8135948a07fe760921732f0364eb0b99d7cf7a8c
    def test_9_to_ix(self):
        self.assertEqual(ar2rom(9), 'ix')

    def test_10_to_x(self):
        self.assertEqual(ar2rom(10), 'x')
=======
    def test_10_to_X(self):
        self.assertEqual(ar2rom(10), 'X')
>>>>>>> Capitalizing roman letter

    def test_20_to_XX(self):
        self.assertEqual(ar2rom(20), 'XX')

    def test_21_to_XXI(self):
        self.assertEqual(ar2rom(21), 'XXI')

if __name__ == "__main__":
    unittest.main()
