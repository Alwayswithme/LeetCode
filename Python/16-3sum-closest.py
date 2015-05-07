#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-07 16:44:21
# Title      :  16 3sum closest


# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
# 
#     For example, given array S = {-1 2 1 -4}, and target = 1.
# 
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        closestDiff = abs(result - target)
        n = len(nums)
        for i in range(n - 2):
            start, end = i + 1, n - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                diff = abs(sum - target)
                if sum == target:
                    return sum

                if diff < closestDiff:
                    result, closestDiff = sum, diff

                if sum < target:
                    start += 1
                elif sum > target:
                    end -= 1

        return result
