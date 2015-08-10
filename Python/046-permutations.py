#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-03 22:39:23
# Title      :  46 permutations

# Given a collection of numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if not nums:
            return nums
        result = []
        self.permuteRecursive(nums, [False for i in range(len(nums))], [], result)
        return result

    def permuteRecursive(self, nums, used, permute, result):
        if len(permute) == len(nums):
            result.append(permute[:])
            return
        for i, num in enumerate(nums):
            if not used[i]:
                used[i] = True
                permute.append(num)
                self.permuteRecursive(nums, used, permute, result)
                permute.pop()
                used[i] = False
