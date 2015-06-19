#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-19 20:04:32
# Title      :  63 unique paths ii

# Follow up for "Unique Paths":
# 
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# For example,
# 
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
# 
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 
# The total number of unique paths is 2.
# 
# Note: m and n will be at most 100.

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        row = [0 for _ in range(len(obstacleGrid[0]))]
        row[0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    # obstacle
                    row[j] = 0
                else:
                    if j > 0:
                        row[j] += row[j - 1]
        return row[-1]
