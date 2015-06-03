#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-03 22:39:23
# Title      :  33 search in rotated sorted array

# uppose a sorted array is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + r >> 1
            if target == nums[m]:
                return m
            if ((nums[m] < nums[r] and target > nums[m] and target <= nums[r]) or
                    (nums[m] >= nums[r] and (target < nums[l] or target >= nums[m]))):
                l = m + 1
            else:
                r = m - 1
        return -1
