#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-11-24 17:27:22
# Title      :  166 fraction to recurring decimal


# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in parentheses.
# 
# For example,
# 
#     Given numerator = 1, denominator = 2, return "0.5".
#     Given numerator = 2, denominator = 1, return "2".
#     Given numerator = 2, denominator = 3, return "0.(6)".
# 
# Credits:
# Special thanks to @Shangrila for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        head, remainder = divmod(numerator, denominator)
        tail, seen = '', {}
        while remainder != 0:
            if remainder in seen:
               tail = tail[: seen[remainder]] + '(' + tail[seen[remainder]:] + ')'
               break
            seen[remainder] = len(tail)
            digit, remainder = divmod(remainder * 10, denominator)
            tail+=str(digit)
        return sign + str(head) + (tail and '.' + tail)
