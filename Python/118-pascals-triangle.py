#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-12 10:55:01
# Title      :  118 pascals triangle


# Given numRows, generate the first numRows of Pascal's triangle.
# 
# For example, given numRows = 5,
# Return
# 
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = []
        for row in range(numRows):
            r.append([])
            for i in range(row + 1):
                if i == 0 or i == row:
                    r[row].append(1)
                else:
                    r[row].append(r[row - 1][i - 1] + r[row - 1][i])
        return r
