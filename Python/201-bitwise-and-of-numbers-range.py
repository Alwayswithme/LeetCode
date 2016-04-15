#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2016-04-14 11:11:54
# Title      :  201 bitwise and of numbers range


# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.
#
# Credits:
# Special thanks to @amrsaqr for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        c = 0
        while m != n:
            m >>= 1
            n >>= 1
            c += 1
        return m << c
