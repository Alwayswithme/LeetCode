#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2016-04-20 19:54:48
# Title      :  217 contains duplicate


# Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
