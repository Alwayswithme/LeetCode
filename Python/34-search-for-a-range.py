#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-31 14:57:47
# Title      :  34 search for a range

# Given a sorted array of integers, find the starting and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4]. 

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        index = self.binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        left, right = index, index
        while left > 0 and nums[left - 1] == nums[index]:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] == nums[index]:
            right += 1
        return [left, right]
        
    def binarySearch(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + high >> 1
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1
