#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-31 15:00:43
# Title      :  35 search insert position

# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# You may assume no duplicates in the array.
# 
# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + high >> 1
            if mid > low and nums[mid] > target and nums[mid-1] < target:
                return mid;
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return low
