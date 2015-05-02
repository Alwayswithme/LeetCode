#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-03 00:39:15
# Title      :  53 maximum subarray

#  Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
# 
# For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
# the contiguous subarray [4,−1,2,1] has the largest sum = 6. 

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        maximum = -1 * (1 << 31)
        sum = 0
        for x in nums:
            sum += x
            maximum = max(sum, maximum)
            if sum < 0:
                sum = 0
        return maximum
