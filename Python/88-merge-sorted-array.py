#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-03 23:34:32
# Title      :  88 merge sorted array

# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# 
# Note:
# You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        i, j = m - 1, n -1
        newLen = m + n -1
        while i >= 0 and j >= 0:
            if A[i] > B[j]:
                A[newLen] = A[i]
                i, newLen = i - 1, newLen -1
            else:
                A[newLen] = B[j]
                j, newLen = j - 1, newLen -1
        while j >= 0:
            A[newLen] = B[j]
            j, newLen = j - 1, newLen -1
