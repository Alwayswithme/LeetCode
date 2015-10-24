#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-11-27 10:29:12
# Title      :  172 factorial trailing zeroes


# Given an integer n, return the number of trailing zeroes in n!.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            n = n/5
            count += n

        return count
