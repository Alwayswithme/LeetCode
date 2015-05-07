#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-07 16:11:50
# Title      :  15 3sum


# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
# 
# Note:
# 
#     Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
#     The solution set must not contain duplicate triplets.
# 
#     For example, given array S = {-1 0 1 2 -1 -4},
# 
#     A solution set is:
#     (-1, 0, 1)
#     (-1, -1, 2)

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        n = len(nums)
        if n < 3:
            return []
        
        unique = set()
        nums.sort()
        for x in range(n):
            target = nums[x]
            negate = -target
            table = {}
            for i in range(x + 1, n):
                number = nums[i]
                if number in table:
                    temp = (target, table[number], number)
                    unique.add(temp)
                table[negate - number] = number
        return list(unique)
