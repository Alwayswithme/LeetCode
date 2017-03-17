#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-19 15:42:23
# Title      :  29 divide two integers

# Divide two integers without using multiplication, division and mod operator.
# 
# If it is overflow, return MAX_INT. 

class Solution(object):
    MAX_INT = (1 << 31) - 1
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1

        result, dvd, dvs = 0, abs(dividend), abs(divisor)
        while dvd >= dvs:
            inc = dvs
            i = 0
            while dvd >= inc:
                dvd -= inc
                result += 1 << i
                inc <<= 1
                i += 1
        result = result if sign == 1 else -result
        if result > Solution.MAX_INT:
            return Solution.MAX_INT
        return result
