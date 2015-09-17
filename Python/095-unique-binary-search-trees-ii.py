#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-17 20:06:31
# Title      :  095 unique binary search trees ii


# Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generate(1, n)

    def generate(self, left, right):
        ret = []
        if left > right:
            ret.append(None)

        for i in range(left, right + 1):
            lList = self.generate(left, i - 1)
            rList = self.generate(i + 1, right)
            for l in lList:
                for r in rList:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ret.append(root)
        return ret
