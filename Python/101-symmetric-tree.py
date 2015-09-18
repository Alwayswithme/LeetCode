#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-18 23:08:00
# Title      :  101 symmetric tree

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        nodes = []
        nodes.append(root)

        level = 1
        while level > 0:
            for i in range(level):
                parent = nodes[i]
                if not parent:
                    continue
                nodes.append(parent.left)
                nodes.append(parent.right)

            start, end = 0, level - 1
            while start < end:
                n1, n2 = nodes[start], nodes[end]
                if (not n1 or not n2) and n1 != n2:
                    return False
                if n1 and n2 and n1.val != n2.val:
                    return False
                start += 1
                end -= 1
            nodes = nodes[level:]
            level = len(nodes)
        return True

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetricRecur(root.left, root.right)

    def isSymmetricRecur(self, left, right):
        if left == right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return (self.isSymmetricRecur(left.left, right.right)
        and self.isSymmetricRecur(left.right, right.left))
