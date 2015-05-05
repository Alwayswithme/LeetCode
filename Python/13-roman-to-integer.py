#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-05 12:20:13
# Title      :  13 roman to integer


# Given a roman numeral, convert it to an integer.
# 
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        romanIntMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0;
        for i in range(len(s) - 1):
            if romanIntMap[s[i]] >= romanIntMap[s[i+1]]:
                res += romanIntMap[s[i]]
            else:
                res -= romanIntMap[s[i]]
        return res + romanIntMap[s[-1]]
