#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-24 11:57:23
# Title      :  #1 two sum

# Given an array of integers, find two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution.
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2 

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for i, number in enumerate(nums):
            if number in table:
                return [table[number] + 1, i + 1]
            table[target - number] = i
