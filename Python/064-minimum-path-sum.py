#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-23 17:14:19
# Title      :  64 minimum path sum

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        row = [0 for i in range(len(grid[0]))]
        row[0] = grid[0][0]
        for i in range(1, len(grid[0])):
            row[i] = row[i - 1] + grid[0][i]
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if j == 0:
                    row[j] += grid[i][j]
                else:
                    row[j] = min(row[j - 1], row[j]) + grid[i][j]
        return row[-1]
