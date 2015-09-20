#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-20 15:50:12
# Title      :  107 binary tree level order traversal ii


# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree {3,9,20,#,#,15,7},
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root:
            return ret
        nodes = [root]
        while nodes:
            levelNodes = []
            length = len(nodes)
            for i in range(length):
                n = nodes[i]
                levelNodes.append(n.val)
                if n.left:
                    nodes.append(n.left)
                if n.right:
                    nodes.append(n.right)
            ret.insert(0, levelNodes)
            nodes = nodes[length:]
        return ret
