#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-04 00:02:23
# Title      :  141 linked list cycle


# Given a linked list, determine if it has a cycle in it.
# 
# Follow up:
# Can you solve it without using extra space? 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None or head.next == None:
            return False
        fast = head
        slow = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
