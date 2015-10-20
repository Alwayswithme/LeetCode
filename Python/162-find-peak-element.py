#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-11-09 18:00:22
# Title      :  162 find peak element


# A peak element is an element that is greater than its neighbors.
# 
# Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
# 
# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
# 
# You may imagine that num[-1] = num[n] = -∞.
# 
# For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
# 
# click to show spoilers.
# Note:
# 
# Your solution should be in logarithmic complexity.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + right >> 1
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
