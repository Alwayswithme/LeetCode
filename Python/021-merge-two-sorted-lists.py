#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-03 23:58:00
# Title      :  21 merge two sorted lists

# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        head.next = l1
        prev = head
        while l1 and l2:
            if l1.val > l2.val:
                nextNode = l2.next
                l2.next = prev.next
                prev.next = l2
                l2 = nextNode
            else:
                l1 = l1.next
            prev = prev.next
        if l2:
            prev.next = l2
        return head.next
