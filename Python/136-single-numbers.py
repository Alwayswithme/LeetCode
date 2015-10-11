#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-22 14:50:28
# Title      :  136 single numbers

# Given an array of integers, every element appears twice except for one. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        return reduce(lambda x, y: x ^ y, nums)
