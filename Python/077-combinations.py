#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-08-07 23:14:03
# Title      :  77 combinations


#  Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
# 
# For example,
# If n = 4 and k = 2, a solution is:
# 
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        ret = []
        self.combineRecursive([], k, 1, n, ret)
        return ret
    
    def combineRecursive(self, l, k, start, n, result):
        if len(l) == k:
            result.append(l[:])
            return
        for i in range(start, n + 1):
            l.append(i)
            self.combineRecursive(l, k, i + 1, n, result)
            l.pop()
