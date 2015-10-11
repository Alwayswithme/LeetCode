#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-22 14:51:13
# Title      :  137 single numbers ii

#  Given an array of integers, every element appears three times except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones = twos = threes = 0
        for n in nums:
            twos |= ones & n
            ones ^= n
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones
