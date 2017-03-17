#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2017-03-18 00:24:30
# Title      :  209 minimum size subarray sum

#  Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
# 
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint. 

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        nLen = len(nums)
        if not nums:
            return 0

        left, right, sum = 0, 0, 0
        minLen = nLen + 1

        while right < nLen:
            sum += nums[right]
            right += 1

            while sum >= s:
                minLen = min(minLen, right - left)
                sum -= nums[left]
                left += 1
        return minLen if minLen != nLen + 1 else 0
