#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-24 23:17:11
# Title      :  113 path sum ii


#  Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# For example:
# Given the below binary tree and sum = 22,
#
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#
# return
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret = []
        self.hasPathSum(root, sum, ret, [])
        return ret
    def hasPathSum(self, root, sum, ret, path):
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            path.append(root.val)
            ret.append(path)
            return True
        sum -= root.val
        path.append(root.val)
        self.hasPathSum(root.left, sum, ret, path[:])
        self.hasPathSum(root.right, sum, ret, path[:])
