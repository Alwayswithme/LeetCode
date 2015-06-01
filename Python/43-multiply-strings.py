#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-01 17:26:11
# Title      :  43 multiply strings

# Given two numbers represented as strings, return multiplication of the numbers as a string.
# 
# Note: The numbers can be arbitrarily large and are non-negative.

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        """
        build-in
        str(int(num1) * int(num2))
        """
        if not num1 or not num2:
            return ''
        if num1 == '0' or num2 == '0':
            return '0'
        result = [0 for i in range(len(num1) + len(num2))]
        for i, n1 in enumerate(num1[::-1]):
            for j, n2 in enumerate(num2[::-1]):
                result[i + j] += int(n1) * int(n2)
        carry, total = 0, []
        for digit in result:
            carry, rem = divmod(carry + digit, 10)
            total.insert(0, str(rem))
        while len(total) > 1 and total[0] == "0":
            del total[0]
        return ''.join(total)
