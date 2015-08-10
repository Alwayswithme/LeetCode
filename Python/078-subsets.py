#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-08-07 23:15:16
# Title      :  78 subsets


# Given a set of distinct integers, nums, return all possible subsets.
#
#Note:
#
#    Elements in a subset must be in non-descending order.
#    The solution set must not contain duplicate subsets.
#
#For example,
#If nums = [1,2,3], a solution is:
#
#[
#  [3],
#  [1],
#  [2],
#  [1,2,3],
#  [1,3],
#  [2,3],
#  [1,2],
#  []
#]

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        subsetList = []
        subsetCount = 1 << len(nums)
        bitset = ["{0:b}".format(i) for i in range(subsetCount)]
        
        for i in range(subsetCount):
            bitStr = bitset[i][::-1]
            s = set()
            for x in range(len(bitStr)):
                if bitStr[x] == '1':
                    s.add(nums[x])
            l = list(s)
            l.sort()
            subsetList.append(l)
        
        return subsetList
