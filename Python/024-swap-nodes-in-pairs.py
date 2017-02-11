#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-22 12:32:47
# Title      :  24 swap nodes in pairs

# Given a linked list, swap every two adjacent nodes and return its head.
# 
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while prev.next is not None and prev.next.next is not None:
            one = prev.next
            two = prev.next.next
            one.next = two.next
            two.next = one
            prev.next = two
            prev = one
        return dummy.next
