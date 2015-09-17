#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-17 20:07:51
# Title      :  096 unique binary search trees


# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        ways = [0 for i in range(n + 1)]
        ways[0] = 1
        ways[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                ways[i] += ways[j] * ways[i - j - 1]
        return ways[n]
