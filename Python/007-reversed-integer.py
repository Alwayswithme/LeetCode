#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-27 23:06:18
# Title      :  7 reversed integer.py

# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = 1
        result = 0
        maxInt = 1 << 31
        if x < 0:
            sign = -1

        num = abs(x)
        while num > 0:
            reminder = num % 10
            if (result > (maxInt - reminder) / 10):
                return 0
            result = result * 10
            result += reminder
            num /= 10

        return sign * result
