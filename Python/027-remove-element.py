#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-18 00:05:38
# Title      :  27 remove element

# Given an array and a value, remove all instances of that value in place and return the new length.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length. 

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        limit = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[limit] = nums[i]
                limit += 1
        return limit
