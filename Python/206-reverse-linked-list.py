#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-05 12:46:13
# Title      :  206 reverse linked list

# Reverse a singly linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None:
            return head
        pre = None
        nex = head.next
        while nex:
            temp = nex.next
            nex.next = head
            head.next = pre
            pre = head
            head = nex
            nex = temp
        return head
