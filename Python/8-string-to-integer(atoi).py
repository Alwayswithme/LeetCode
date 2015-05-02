#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-03 01:56:00
# Title      :  8 string to integer(atoi)

# Implement atoi to convert a string to an integer.
# 
# Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# 
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
# 
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition. 

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        INT_MAX, INT_MIN = 2147483647, -2147483648
        strLen = len(str)
        if strLen == 0:
            return 0
        i,result = 0, 0

        sign = 1
        while i < strLen and str[i] == ' ':
            i += 1
        if str[i] in ('+', '-'):
            if str[i] == '-':
                sign = -1
            i += 1

        while i < strLen and str[i].isdigit():
            result = result * 10 + ord(str[i]) - ord('0')
            if result > INT_MAX:
                return INT_MAX if sign > 0 else INT_MIN
            i += 1
        
        return result * sign
