#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-20 15:47:39
# Title      :  105 construct binary tree from preorder and inorder traversal

# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree. 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dict = {}
        for i, v in enumerate(inorder):
            dict[v] = i
        return self.buildTreeRecur(dict, preorder, inorder, 0, len(inorder) - 1, 0)
        
    def buildTreeRecur(self, dict, preorder, inorder, inStart, inEnd, preStart):
        if inStart > inEnd:
            return None
        val = preorder[preStart]
        root, i = TreeNode(val), dict[val]
        root.left = self.buildTreeRecur(dict, preorder, inorder, inStart, i - 1, preStart + 1)
        root.right = self.buildTreeRecur(dict, preorder, inorder, i + 1, inEnd, preStart + 1 + i - inStart)
        return root
