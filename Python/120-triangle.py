#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-12 15:02:24
# Title      :  120 triangle

# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
# 
# For example, given the following triangle
# 
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
# 
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. 

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        triangle = triangle[::-1]
        total = triangle.pop(0)
        for row in triangle:
            for i, val in enumerate(row):
                total[i] = min(total[i], total[i + 1]) + val
        return total[0]
