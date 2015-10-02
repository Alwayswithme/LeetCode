#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-08 13:42:43
# Title      :  117 populating next right pointers in each node ii


# Follow up for problem "Populating Next Right Pointers in Each Node".
# 
# What if the given tree could be any binary tree? Would your previous solution still work?
# 
# Note:
# 
#     You may only use constant extra space.
# 
# For example,
# Given the following binary tree,
# 
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# 
# After calling your function, the tree should look like:
# 
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL

# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        while root:
            root = self.connectNode(root)
    
    def connectNode(self, root):
        pre = None
        first = None
        while root:
            if root.left:
                if not pre:
                    first = pre = root.left
                else:
                    pre.next = root.left
                    pre = root.left
            if root.right:
                if not pre:
                    first = pre = root.right
                else:
                    pre.next = root.right
                    pre = root.right
            root = root.next
        return first
