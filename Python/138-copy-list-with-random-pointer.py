#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2017-02-10 13:08:21
# Title      :  138 copy list with random pointer

# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
#
# Return a deep copy of the list.
#

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        old_node = head
        while old_node:
            new_node = RandomListNode(old_node.label)
            new_node.next = old_node.next
            old_node.next = new_node
            old_node = new_node.next
        
        old_node = head
        while old_node:
            new_node = old_node.next
            if old_node.random:
                new_node.random = old_node.random.next
            old_node = new_node.next
            
        new_head = head.next
        old_node = head
        while old_node:
            new_node = old_node.next
            old_node.next = new_node.next
            if new_node.next:
                new_node.next = new_node.next.next
            old_node = old_node.next
        
        return new_head
