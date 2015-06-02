#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-02 18:08:38
# Title      :  67 add binary

# Given two binary strings, return their sum (also a binary string).
# 
# For example,
# a = "11"
# b = "1"
# Return "100". 

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        if not a or not b:
            return '0'
        a, b = a[::-1], b[::-1]
        a_len, b_len = len(a), len(b)
        if a_len < b_len:
            a, b = b, a
            a_len, b_len = b_len, a_len
        carry, res = 0, ''
        for i in range(b_len):
            carry, rem = divmod((carry + int(a[i]) + int(b[i])), 2)
            res += str(rem)

        for i in range(b_len, a_len):
            carry, rem = divmod((carry + int(a[i])), 2)
            res += str(rem)

        if carry == 1:
            res += '1'
        return res[::-1]
