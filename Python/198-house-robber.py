#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-12-01 17:43:22
# Title      :  198 house robber


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
# 
# Credits:
# Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.
# 
# Subscribe to see which companies asked this question


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        prev2 = nums[0]
        prev1 = max(nums[:2])
        for i in range(2, len(nums)):
            prev1, prev2 = max(prev1, prev2 + nums[i]), prev1
        return prev1
