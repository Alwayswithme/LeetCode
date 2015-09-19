#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-19 21:05:32
# Title      :  103 binary tree zigzag level order traversal


# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
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
# return its zigzag level order traversal as:
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ret = []
        nodes = [root]
        zig = 1
        while nodes:
            vals, n = [], len(nodes)
            for i in range(n):
                node = nodes[i]
                vals.append(node.val)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            ret.append(vals[::zig])
            zig *= -1
            nodes = nodes[n:]
        return ret
