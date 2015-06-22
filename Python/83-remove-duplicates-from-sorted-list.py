#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-05 22:10:23
# Title      :  83 remove duplicates from sorted list

# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return head
        prev = head
        cur = head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
                cur.next = None
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return head
