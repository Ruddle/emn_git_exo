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
    def test_1_to_i(self):
        self.assertEqual(ar2rom(1), 'i')

    def test_2_to_ii(self):
        self.assertEqual(ar2rom(2), 'ii')

    def test_3_to_iii(self):
        self.assertEqual(ar2rom(3), 'iii')

    def test_4_to_iv(self):
        self.assertEqual(ar2rom(4), 'iv')

    def test_5_to_v(self):
        self.assertEqual(ar2rom(5), 'v')

    def test_9_to_ix(self):
        self.assertEqual(ar2rom(9), 'ix')

    def test_10_to_x(self):
        self.assertEqual(ar2rom(10), 'x')

    def test_20_to_xx(self):
        self.assertEqual(ar2rom(20), 'xx')

    def test_21_to_xxi(self):
        self.assertEqual(ar2rom(21), 'xxi')

if __name__ == "__main__":
    unittest.main()
