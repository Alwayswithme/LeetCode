#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-18 20:31:23
# Title      :  22 generate parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# "((()))", "(()())", "(())()", "()(())", "()()()"

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        result = []
        self.recursiveCall(result, "", n, n)
        return result

    def recursiveCall(self, result, current, left, right):
        if left == 0 and right == 0:
            result.append(current)
        if left > 0:
            self.recursiveCall(result, current + "(", left - 1, right)
        if left < right:
            self.recursiveCall(result, current + ")", left, right - 1)
