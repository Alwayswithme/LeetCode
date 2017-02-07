#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-27 23:06:18
# Title      :  7 reversed integer.py

# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        result = 0
        max = 1 << 31
        
        num = abs(x)
        while num > 0:
            num, reminder = divmod(num, 10)
            if (result > (max - reminder) / 10):
                return 0
            result = result * 10 + reminder
        
        return sign * result
