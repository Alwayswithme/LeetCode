#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2017-04-28 20:44:14
# Title      :  222 count complete tree node

# Given a complete binary tree, count the number of nodes.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        leftDepth = self.getDepth(root, True)
        rightDepth = self.getDepth(root, False)
        if leftDepth == rightDepth:
            return (1 << leftDepth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def getDepth(self, root, left):
        if not root:
            return 0
        dep = 0
        while root:
            dep += 1
            if left:
                root = root.left
            else:
                root = root.right
        return dep
