#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-18 00:05:38
# Title      :  27 remove element

# Given an array and a value, remove all instances of that value in place and return the new length.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length. 

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
            if i >= len(nums):
                break
        return len(nums)
