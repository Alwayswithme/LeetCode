#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-22 13:58:52
# Title      :  31 next permutation

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place, do not allocate extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n = len(nums)
        k, l = -1, 0
        for i in range(n-1):
            if (nums[i]<nums[i+1]):
                k = i
                
        if k == -1:
            # not possible
            nums.sort()
            return
        for i in range(n):
            if nums[i] > nums[k]:
                l = i
        nums[k], nums[l] = nums[l], nums[k]
        rev_nums = nums[:k:-1]
        for i in range(len(rev_nums)):
            nums[k + 1 + i] = rev_nums[i]
