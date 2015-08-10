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
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev, i = dummy, 0
        while head:
            i += 1
            if (i & 1) == 0:
                #even
                prev.next.next = head.next
                head.next = prev.next
                prev.next = head
                prev = head.next
                head = prev.next
            else:
                head = head.next
        return dummy.next
