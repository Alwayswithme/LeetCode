#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-26 17:25:14
# Title      :  89 gray code

# The gray code is a binary numeral system where two successive values differ in only one bit.
# 
# Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
# 
# For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
# 
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
# 
# Note:
# For a given n, a gray code sequence is not uniquely defined.
# 
# For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.
# 
# For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        result = [0]
        for i in xrange(0, n):
            for x in reversed(result):
                result.append(1 << i | x)
        return result
