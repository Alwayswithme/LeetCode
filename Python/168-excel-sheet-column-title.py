#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-24 11:02:58
# Title      :  #168 excel sheet column title

# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# 
# For example:
# 
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
# 
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases.

class Solution:
    # @return a string
    def convertToTitle(self, num):
        r = ''
        while (num):
            num -= 1
            r = getChar(num) + r
            num /= 26

        return r


def getChar(n):
    return chr(ord('A')+(n)%26)
