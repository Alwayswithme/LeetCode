#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-21 10:42:01
# Title      :  39 combination sum

# Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# 
# The same repeated number may be chosen from C unlimited number of times.
# 
# Note:
# 
#     All numbers (including target) will be positive integers.
#     Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#     The solution set must not contain duplicate combinations.
# 
# For example, given candidate set 2,3,6,7 and target 7,
# A solution set is:
# [7]
# [2, 2, 3]

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.combineRecursive(result, 0, candidates, target, [])
        return result
    
    def combineRecursive(self, result, start, candidates, target, comb):
        if target == 0:
            result.append(comb)
            return
        
        for i in xrange(start, len(candidates)):
            new_comb = comb[:]
            if candidates[i] > target:
                return
            new_comb.append(candidates[i])
            self.combineRecursive(result, i, candidates, target - candidates[i], new_comb)
