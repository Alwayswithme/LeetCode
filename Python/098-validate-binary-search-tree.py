#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-17 20:10:24
# Title      :  098 validate binary search tree


#  Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bignum = 1 << 63
        return self.isValid(-bignum, bignum, root)

    def isValid(self, left, right, node):
        if not node:
            return True
        v = node.val
        if v <= left or v >= right:
            return False
        return self.isValid(left, v, node.left) and self.isValid(v, right, node.right)
