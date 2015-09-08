#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-09-08 23:31:47
# Title      :  091 decode ways


#  A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
#

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n1 = n2 = 1
        ways = 1
        for i in range(len(s)):
            num = int(s[i])
            if i > 0:
                num += int(s[i-1]) * 10
            if num % 10 == 0 and num not in (10, 20):
                return 0
            if (num > 10 and num < 20) or (num > 20 and num < 27):
                ways = n1 + n2
            if (num > 0 and num < 10) or (num > 27):
                ways = n2
            if num == 10 or num == 20:
                ways = n1
            n1 = n2
            n2 = ways
        return ways
