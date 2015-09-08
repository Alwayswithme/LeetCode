#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-08 23:30:41
# Title      :  090 subsets ii


#  Given a collection of integers that might contain duplicates, nums, return all possible subsets.
#
# Note:
#
#     Elements in a subset must be in non-descending order.
#     The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsetSet = set()
        subsetCount = 1 << len(nums)

        for i in range(subsetCount):
            s = []
            for x in range(i.bit_length()):
                if i & (1 << x) != 0:
                    s.append(nums[x])
            s.sort()
            subsetSet.add(tuple(s))

        return [list(i) for i in subsetSet]
