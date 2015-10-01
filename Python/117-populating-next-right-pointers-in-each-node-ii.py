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
        if not root:
            return
        nodes = [root]
        while nodes:
            self.connectNode(nodes)
            size = len(nodes)
            for i in range(size):
                n = nodes[i]
                if n.left:
                    nodes.append(n.left)
                if n.right:
                    nodes.append(n.right)
            nodes = nodes[size:]
    
    def connectNode(self, nodes):
        pre = None
        for i in reversed(nodes):
            i.next = pre
            pre = i
