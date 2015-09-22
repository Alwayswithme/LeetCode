#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-22 16:13:16
# Title      :  109 convert sorted list to binary search tree

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        current, length = head, 0
        while current:
            current, length = current.next, length + 1
        self.head = head
        return self.bst(0, length - 1)
    
    def bst(self, start, end):
        if start > end:
            return None
        mid = start + end >> 1
        left = self.bst(start, mid - 1)
        listNode = self.head
        current = TreeNode(listNode.val)
        current.left = left 
        self.head = listNode.next
        current.right = self.bst(mid + 1, end)
        return current
