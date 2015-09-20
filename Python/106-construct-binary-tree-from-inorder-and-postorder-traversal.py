#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-20 15:48:44
# Title      :  106 construct binary tree from inorder and postorder traversal

# Given inorder and postorder traversal of a tree, construct the binary tree.
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        dict = {}
        for i, v in enumerate(inorder):
            dict[v] = i
        return self.buildTreeRecur(dict, inorder, postorder, 0, len(inorder) - 1, len(postorder) -1)
    
    def buildTreeRecur(self, dict, inorder, postorder, inStart, inEnd, postStart):
        if inStart > inEnd:
            return None
        val = postorder[postStart]
        root, i = TreeNode(val), dict[val]
        root.left = self.buildTreeRecur(dict, inorder, postorder, inStart, i - 1, postStart - 1 - (inEnd - i))
        root.right = self.buildTreeRecur(dict, inorder, postorder, i + 1, inEnd, postStart -1)
        return root
