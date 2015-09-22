#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-22 16:14:06
# Title      :  018 4sum


# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# 
# Note:
# 
#     Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
#     The solution set must not contain duplicate quadruplets.
# 
#     For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
# 
#     A solution set is:
#     (-1,  0, 0, 1)
#     (-2, -1, 1, 2)
#     (-2,  0, 0, 2)

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums, result = sorted(nums), set()
        for i, v in enumerate(nums):
            l = self.threeSum(nums, target - v, i + 1)
            fSum = [(v,) + tup for tup in l]
            result.update(fSum)
        return list(result)

    def threeSum(self, nums, target, start):
        unique = set()
        n = len(nums)
        for x in range(start, n):
            find = (target - nums[x])
            table = {}
            for i in range(x + 1, n):
                number = nums[i]
                if number in table:
                    temp = (nums[x], table[number], number)
                    unique.add(temp)
                table[find - number] = number
        return list(unique)
