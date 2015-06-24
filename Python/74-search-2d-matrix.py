#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-24 17:59:27
# Title      :  74 search 2d matrix

# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# 
#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.
# 
# For example,
# 
# Consider the following matrix:
# 
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# 
# Given target = 3, return true.

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if target < matrix[i][j]:
                j -= 1
            elif target > matrix[i][j]:
                i += 1
            else:
                return True
        return False
