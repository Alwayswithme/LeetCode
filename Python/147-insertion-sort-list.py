#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-28 12:57:08
# Title      :  147 insertion sort list


# Sort a linked list using insertion sort.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or self.isSorted(head):
            return head
        dummy = ListNode(-1)
        pre = dummy
        
        while head:
            pre = dummy
            while pre.next and pre.next.val <= head.val:
                pre = pre.next
            head.next, pre.next, head = pre.next, head, head.next

        return dummy.next
        
    def isSorted(self, head):
        while head and head.next:
            if head.val > head.next.val:
                return False
            head = head.next
        return True

