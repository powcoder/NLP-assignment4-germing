https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

import unittest

from regular import is_arithmetic_expression, is_date


class Test_is_arithmetic_expression(unittest.TestCase):

    def test1(self):
        self.assertEqual(is_arithmetic_expression('1*8'), True)

    def test2(self):
        self.assertEqual(is_arithmetic_expression('1*8+17'), True)

    def test3(self):
        self.assertEqual(is_arithmetic_expression('100'), False)

    def test4(self):
        self.assertEqual(is_arithmetic_expression('1*+8'), False)

    def test5(self):
        self.assertEqual(is_arithmetic_expression('a 1+8'), False)



if __name__ == '__main__':

    unittest.main()
