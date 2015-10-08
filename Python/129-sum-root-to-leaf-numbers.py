#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-13 16:09:20
# Title      :  129 sum root to leaf numbers

# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# 
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# 
# Find the total sum of all root-to-leaf numbers.
# 
# For example,
# 
#     1
#    / \
#   2   3
# 
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# 
# Return the sum = 12 + 13 = 25. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumRecur(0, root)

    def sumRecur(self, prev, node):
        if not node:
            return 0
        curSum = prev * 10 + node.val
        if not node.left and not node.right:
            return curSum
        return self.sumRecur(curSum, node.left) + self.sumRecur(curSum, node.right)
