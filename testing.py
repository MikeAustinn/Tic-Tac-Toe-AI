""" Add a test for notable functions bellow """

import unittest
import functions as f


class FunctionTesting(unittest.TestCase):
    
    def test_take_move(self):
        old = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        new = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(f.take_move(old, 1, 1), new)

    def test_win_check(self):
        o_win = [2, 2, 2, 0, 1, 0, 0, 1, 1]
        self.assertEqual(f.win_check(o_win), 2)
        x_win = [1, 1, 1, 0, 2, 0, 0, 2, 0]
        self.assertEqual(f.win_check(x_win), 1)
        no_win = [1, 2, 1, 1, 2, 2, 0, 2, 1]
        self.assertEqual(f.win_check(no_win), 0)

if __name__ == '__main__':
    unittest.main()

    
    
    
