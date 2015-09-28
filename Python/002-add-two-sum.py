#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-24 12:13:36
# Title      :  #2 add two sum

# You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        gt10 = 0
        cursor = dummy
        while l1 or l2:
            val = gt10
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            gt10, val = divmod(val, 10)
            cursor.next = ListNode(val)
            cursor = cursor.next
        if gt10 > 0:
            cursor.next = ListNode(gt10)
        return dummy.next
