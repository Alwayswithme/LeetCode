#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-18 15:35:20
# Title      :  70 climbing stairs

# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n < 3:
            return n
        x1 = 1
        x2 = 2
        for i in range(3, n + 1):
            x1, x2 = x2, x1 + x2
        return x2
