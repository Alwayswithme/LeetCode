#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-28 17:56:10
# Title      :  148 sort list


# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Subscribe to see which companies asked this question


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        fast, slow, prev = head, head, None
        while fast != None and fast.next != None:
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None
        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)
        return self.mergeTwoLists(sorted_l1, sorted_l2)        
        
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        current = head
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                current.next, current, l1 = l1, l1, l1.next
            else:
                current.next, current, l2 = l2, l2, l2.next
        if l1 != None:
            current.next = l1
        if l2 != None:
            current.next = l2
        return head.next

