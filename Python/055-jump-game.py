#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-17 13:58:30
# Title      :  55 jump game

# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# 
# Each element in the array represents your maximum jump length at that position.
# 
# Determine if you are able to reach the last index.
# 
# For example:
# A = [2,3,1,1,4], return true.
# 
# A = [3,2,1,0,4], return false. 

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        if not nums:
            return False
        i, max_jump, n = 0, 0, len(nums)
        if nums[0] > n:
            return True
        while i <= max_jump and max_jump < n -1:
            max_jump = max(max_jump, nums[i] + i)
            i += 1
        if max_jump >= n - 1:
            return True
        return False
