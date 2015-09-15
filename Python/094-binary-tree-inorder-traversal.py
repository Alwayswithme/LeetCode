#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-15 23:25:37
# Title      :  094 binary tree inorder traversal

# Given a binary tree, return the inorder traversal of its nodes' values.
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
# return [1,3,2].
#
# Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.traverRecursive(root, result)
        return result

    def traverRecursive(self, node, result):
        if node:
            self.traverRecursive(node.left, result)
            result.append(node.val)
            self.traverRecursive(node.right, result)

# iteratively:
    def inorderTraversal(self, root):
        stack = []
        node = root
        result = []
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result
