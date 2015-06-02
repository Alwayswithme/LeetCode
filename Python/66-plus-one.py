#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-02 18:07:06
# Title      :  66 plus one

# Given a non-negative number represented as an array of digits, plus one to the number.
# 
# The digits are stored such that the most significant digit is at the head of the list.

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if not digits:
            return digits
        for i in range(len(digits) - 1, -1, -1):
            (num, rem) = divmod((digits[i] + 1), 10)
            digits[i] = rem
            if num == 0:
                return digits

        digits.insert(0, 1)
        return digits
