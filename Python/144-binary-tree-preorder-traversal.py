#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-28 11:06:30
# Title      :  144 binary tree preorder traversal

# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# For example:
# Given binary tree {1,#,2,3},
# 
#    1
#     \
#      2
#     /
#    3
# 
# return [1,2,3].
# 
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, ret = [root], []

        while stack and root:
            root = stack.pop(0)
            ret.append(root.val)
            if root.right:
                stack = [root.right] + stack
            if root.left:
                stack = [root.left] + stack

        return ret
