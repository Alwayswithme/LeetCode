#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-29 23:57:23
# Title      :  69 sqrtx

# Implement int sqrt(int x).
#
# Compute and return the square root of x.

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x == 0 or x == 1:
            return x

        guess = 1.0
        while not abs(guess * guess - x) / x < 0.00001:
            guess = (guess + x / guess) / 2

        result = int(guess)
        if (result * result) > x:
            return result - 1
        return result
