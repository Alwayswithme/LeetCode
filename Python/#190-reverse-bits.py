#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-24 10:37:39
# Title      :  #190 reverse bits

# Reverse bits of a given 32 bits unsigned integer.
# 
# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).
# 
# Follow up:
# If this function is called many times, how would you optimize it?
# 
# Related problem: Reverse Integer
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # cast n to bin, remove the 0b and fill with zero
        v=bin(n)[2:].zfill(32)
        # reverse bits
        r=v[::-1]
        return int(r, 2)
