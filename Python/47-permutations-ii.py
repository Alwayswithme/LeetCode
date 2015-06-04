#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-04 22:24:23
# Title      :  46 permutations

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [1,1,2], [1,2,1], and [2,1,1].

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        if not nums:
            return nums
        result = []
        self.permuteRecursive(sorted(nums), [False for i in range(len(nums))], [], result)
        return result
    def permuteRecursive(self, nums, used, permute, result):
        if len(permute) == len(nums):
            result.append(permute[:])
            return
        for i, num in enumerate(nums):
            if i > 0 and not used[i -1] and nums[i] == nums[i - 1]:
                continue
            if not used[i]:
                used[i] = True
                permute.append(num)
                self.permuteRecursive(nums, used, permute, result)
                permute.pop()
                used[i] = False
