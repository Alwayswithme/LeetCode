#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-17 13:57:41
# Title      :  54 spiral matrix

# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
# 
# For example,
# Given the following matrix:
# 
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 
# You should return [1,2,3,6,9,8,7,4,5]. 

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        spiral = []
        try:
            while True:
                spiral += matrix.pop(0)
                for i in range(len(matrix)):
                    spiral.append(matrix[i].pop(-1))
                spiral += reversed(matrix.pop(-1))
                for i in range(len(matrix) - 1, -1, -1):
                    spiral.append(matrix[i].pop(0))
        except:
            pass
        return spiral
