#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-01 16:40:06
# Title      :  41 first missing positive

# Given an unsorted integer array, find the first missing positive integer.
# 
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 
# Your algorithm should run in O(n) time and uses constant space. 

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        i, n = 0, len(nums)
        while i < n:
            if nums[i] > 0 and nums[i] - 1 < n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
