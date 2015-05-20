#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-20 21:31:13
# Title      :  25 reverse nodes in k group

# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
#
# You may not alter the values in the nodes, only nodes itself may be changed.
#
# Only constant memory is allowed.
#
# For example,
# Given this linked list: 1->2->3->4->5
#
# For k = 2, you should return: 2->1->4->3->5
#
# For k = 3, you should return: 3->2->1->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        i = 0
        while head:
            i += 1
            if (i % k) == 0:
                prev = self.reverseLinklist(prev, head.next)
                head = prev.next
            else:
                head = head.next
                return dummy.next

    """
    Reverse a Linked list from prev to end
    return last node after reverse
    """
    def reverseLinklist(self, prev, end):
        last = prev.next
        cur = last.next
        while cur != end:
            last.next = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = last.next
        return last
