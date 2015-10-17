#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-29 17:13:00
# Title      :  150 evaluate reverse polish notation


#  Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# 
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# 
# Some examples:
# 
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack, operators = [], {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}
        for op in tokens:
            if op in ('+', '-', '*', '/'):
                n1, n2 = stack.pop(), stack.pop()
                stack.append(int(operators[op](n2 * 1.0, n1)))
            else:
                stack.append(int(op))
        return stack.pop()
