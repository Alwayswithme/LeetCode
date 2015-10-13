#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-22 17:17:28
# Title      :  142 linked list cycle ii

#  Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# 
# Note: Do not modify the linked list.
# 
# Follow up:
# Can you solve it without using extra space?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None
