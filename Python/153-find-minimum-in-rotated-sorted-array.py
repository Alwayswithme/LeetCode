#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-11-24 16:45:27
# Title      :  153 find minimum in rotated sorted array


# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Subscribe to see which companies asked this question


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + r >> 1
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]
