#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2016-04-20 19:56:48
# Title      :  231 power of two

#Given an integer, write a function to determine if it is a power of two.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & (n-1)) == 0
