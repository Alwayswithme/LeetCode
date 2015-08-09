#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-08-10 21:01:29
# Title      :  080 remove duplicates from sorted array ii

#  Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# 
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length. 

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i = 1
        prev = nums[0]
        twice = False
        while i < len(nums):
            if nums[i] == prev and twice:
                nums.pop(i)
            elif nums[i] == prev and not twice:
                twice = True
                i += 1
            else:
                prev = nums[i]
                twice = False
                i += 1
        return i
