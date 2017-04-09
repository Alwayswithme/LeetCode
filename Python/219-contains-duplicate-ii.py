#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2017-04-09 12:43:25
# Title      :  219 contains duplicate ii

# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k. 

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash = {}
        for i, num in enumerate(nums):
            if num in hash:
                diff = abs(i - hash[num])
                if diff <= k:
                    return True
                else:
                    hash[num] = i
            else:
                hash[num] = i
        return False
