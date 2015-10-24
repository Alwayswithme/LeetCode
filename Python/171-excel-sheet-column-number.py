#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-11-27 10:22:34
# Title      :  171 excel sheet column number


# Related to question Excel Sheet Column Title
# 
# Given a column title as appear in an Excel sheet, return its corresponding column number.
# 
# For example:
# 
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        for i, v in enumerate(s[::-1]):
            ret += (ord(v) - 64) * (26 ** i)
        return ret
