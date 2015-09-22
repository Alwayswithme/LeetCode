#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-22 16:12:20
# Title      :  108 convert sorted array to binary search tree

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        return self.bst(nums, 0, len(nums) - 1)

    def bst(self, nums, low, high):
        if low > high:
            return None
        mid = (low + high) >> 1
        node = TreeNode(nums[mid])
        node.left = self.bst(nums, low, mid - 1)
        node.right = self.bst(nums, mid + 1, high)
        return node
