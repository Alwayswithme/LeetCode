#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-14 23:31:21
# Title      :  019 remove nth node from end of list

# Given a linked list, remove the nth node from the end of list and return its head.
# 
# For example,
# 
#    Given linked list: 1->2->3->4->5, and n = 2.
# 
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# 
# Note:
# Given n will always be valid.
# Try to do this in one pass. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        
        for i in range(n):
            fast = fast.next
        
        while fast.next:
            slow, fast = slow.next, fast.next
            
        nth = slow.next
        slow.next = nth.next
        nth.next = None
        return dummy.next
