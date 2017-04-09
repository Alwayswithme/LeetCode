#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2017-04-09 12:38:54
# Title      :  216 combination sum iii


# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# 
# Example 1:
# 
# Input: k = 3, n = 7
# 
# Output:
# 
# [[1,2,4]]
# 
# 
# Example 2:
# 
# Input: k = 3, n = 9
# 
# Output:
# 
# [[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.combi(k, n, 1, result, [])
        
        return result
    
    def combi(self, k, n, start, result, l):
        if len(l) + 1 == k:
            last = n - sum(l)
            if 10 > last >= start:
                l.append(last)
                result.append(l)
            return
        for i in range(start, 10):
            newList = l + [i]
            self.combi(k, n, i + 1, result, newList)
