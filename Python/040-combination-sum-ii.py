#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-21 10:49:22
# Title      :  40 combination sum ii

# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# 
# Each number in C may only be used once in the combination.
# 
# Note:
# 
#     All numbers (including target) will be positive integers.
#     Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
#     The solution set must not contain duplicate combinations.
# 
# For example, given candidate set 10,1,2,7,6,1,5 and target 8,
# A solution set is:
# [1, 7]
# [1, 2, 5]
# [2, 6]
# [1, 1, 6] 

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.combineRecursive(result, 0, candidates, target, [])
        return result
    
    def combineRecursive(self, result, start, candidates, target, comb):
        if target == 0:
            if comb not in result:
                result.append(comb)
            return
        
        for i in xrange(start, len(candidates)):
            new_comb = comb[:]
            if candidates[i] > target:
                return
            new_comb.append(candidates[i])
            self.combineRecursive(result, i + 1, candidates, target - candidates[i], new_comb)
