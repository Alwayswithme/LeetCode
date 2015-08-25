#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-08-26 01:14:52
# Title      :  082 remove duplicates from sorted list ii

#  Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# 
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3. 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        deleteCur = False
        cur = head
        prev = ListNode(0)
        prev.next = cur

        while cur.next:
            n = cur.next
            if n.val == cur.val:
                cur.next = n.next
                n.next = None
                deleteCur = True
            else:
                if deleteCur:
                    deleteCur = False
                    if cur == head:
                        head = cur.next
                    cur.next = None
                    prev.next = n
                    cur = n
                else:
                    prev = cur
                    cur = n
        if deleteCur:
            if cur == head:
                head = cur.next
            prev.next = None
        return head
