#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-16 23:47:00
# Title      :  100 same tree

#  Given two binary trees, write a function to check if they are equal or not.
# 
# Two binary trees are considered equal if they are structurally identical and the nodes have the same value. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p or not q:
            return p == q
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
