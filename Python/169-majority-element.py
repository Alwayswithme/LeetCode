#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-11-25 17:59:37
# Title      :  169 majority element


# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always exist in the array.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        time, num = 0, 0
        for v in nums:
            if time == 0:
                num = v
            if num == v:
                time += 1
            else:
                time -= 1
        return num
