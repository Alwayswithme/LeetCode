#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-30 16:38:48
# Title      :  152 maximum product subarray


#  Find the contiguous subarray within an array (containing at least one number) which has the largest product.
# 
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        product, maxProduct, minProduct = 1, 1, 1
        largest = float("-inf")
        for val in nums:
            maxProduct, minProduct = max(val, val * maxProduct, val * minProduct), min(val, val * maxProduct, val * minProduct)
            largest = max(largest, maxProduct)
        return largest
