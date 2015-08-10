#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-18 15:33:09
# Title      :  61 rotate list

# Given a list, rotate the list to the right by k places, where k is non-negative.
# 
# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head or k == 0:
            return head
        fast = head
        length = 1
        # count length
        while fast.next:
            fast = fast.next
            length += 1
        k %= length
        if k == 0:
            # no change
            return head
        fast.next = head
        for i in range(length - k):
            fast = fast.next
        newHead = fast.next
        fast.next = None
        return newHead
