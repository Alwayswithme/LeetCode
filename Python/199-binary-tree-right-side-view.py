#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2016-04-14 11:06:13
# Title      :  199 binary tree right side view


# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# For example:
# Given the following binary tree,
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#
# You should return [1, 3, 4].
#
# Credits:
# Special thanks to @amrsaqr for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.dfs(root, res, 1)
        return res

    def dfs(self, node, res, level):
        if not node:
            return
        if level > len(res):
            res.append(node.val)
        self.dfs(node.right, res, level + 1)
        self.dfs(node.left, res, level + 1)
