#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-18 15:31:04
# Title      :  59 spiral matrix ii

# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
# 
# For example,
# Given n = 3,
# You should return the following matrix:
# 
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        matrix = [[0 for x in range(n)] for x in range(n)]
        num = 1
        for l in range(n/2):
            # top
            for i in range(l, n - l):
                matrix[l][i] = num
                num += 1
            # right
            for i in range(l + 1, n - l):
                matrix[i][n - l - 1] = num
                num += 1
            # bottom
            for i in range(n - l - 2, l, -1):
                matrix[n - l - 1][i] = num
                num += 1
            # left
            for i in range(n - l - 1, l, -1):
                matrix[i][l] = num
                num += 1
        if n % 2 == 1:
            matrix[n // 2][n // 2] = num
        return matrix
