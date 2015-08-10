#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-24 17:58:33
# Title      :  73 set matrix zeroes

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place. 

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        first_row = reduce(lambda acc, i: acc or matrix[0][i] == 0, range(len(matrix[0])), False)
        first_col = reduce(lambda acc, i: acc or matrix[i][0] == 0, range(len(matrix)), False)
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0], matrix[0][j] = 0, 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                     matrix[i][j] = 0
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if first_row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
