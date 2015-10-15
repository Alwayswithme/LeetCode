#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-28 11:11:01
# Title      :  145 binary tree postorder traversal

# Given a binary tree, return the postorder traversal of its nodes' values.
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
# return [3,2,1].
# 
# Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack, current, prev = [], [], root, None
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                parent = stack[-1]
                if parent.right in (None, prev):
                    prev = stack.pop()
                    res.append(prev.val)
                else:
                    current = parent.right
        return res
