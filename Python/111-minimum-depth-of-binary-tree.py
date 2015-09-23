#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-23 21:45:35
# Title      :  111 minimum depth of binary tree

# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the root
# node down to the nearest leaf node.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDepth(root)

    def getDepth(self, node):
        if not node:
            return 0
        if not node.left:
            return self.getDepth(node.right) + 1
        if not node.right:
            return self.getDepth(node.left) + 1
        left = self.getDepth(node.left)
        right = self.getDepth(node.right)

        return min(left, right) + 1
