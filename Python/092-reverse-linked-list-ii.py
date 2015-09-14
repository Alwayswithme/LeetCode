#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-14 23:56:48
# Title      :  092 reverse linked list ii


#  Reverse a linked list from position m to n. Do it in-place and in one-pass.
# 
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
# 
# return 1->4->3->2->5->NULL.
# 
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.
# 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev, current = dummy, head
        # find begin
        i = 1
        while current and i != m:
            i += 1
            prev, current = current, current.next
        begin_prev, begin = prev, current
        while current and i <= n:
            i += 1
            current.next, prev, current = prev, current, current.next
        begin.next, begin_prev.next = current, prev
        return dummy.next
