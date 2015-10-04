#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-12 10:56:04
# Title      :  119 pascals triangle ii

# Given an index k, return the kth row of the Pascal's triangle.
# 
# For example, given k = 3,
# Return [1,3,3,1].
# 
# Note:
# Could you optimize your algorithm to use only O(k) extra space? 

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in range(rowIndex):
            result = [1] + [result[j - 1] + result[j] for j in range(1, i + 1)] + [1]
        return result
