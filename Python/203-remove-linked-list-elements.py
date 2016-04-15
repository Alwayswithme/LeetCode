#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2016-04-13 23:57:23
# Title      :  203 remove linked list element


# Remove all elements from a linked list of integers that have value val.
#
# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        ptr = dummy = ListNode(0)
        dummy.next = head
        while ptr.next:
            if ptr.next.val == val:
                next = ptr.next
                ptr.next = next.next
                next.next = None
            else:
                ptr = ptr.next
        return dummy.next
