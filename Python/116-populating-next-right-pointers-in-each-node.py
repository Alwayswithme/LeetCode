#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-08 13:23:10
# Title      :  116 populating next right pointers in each node


#  Given a binary tree
# 
#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# 
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
#     You may only use constant extra space.
#     You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# 
# For example,
# Given the following perfect binary tree,
# 
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# 
# After calling your function, the tree should look like:
# 
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL

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
