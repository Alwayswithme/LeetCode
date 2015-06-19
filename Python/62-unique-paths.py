#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-19 20:02:44
# Title      :  62 unique paths

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 3 x 7 grid. How many possible unique paths are there?
# 
# Note: m and n will be at most 100.

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        row = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]
