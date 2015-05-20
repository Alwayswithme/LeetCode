#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-20 15:22:38
# Title      :  38 count and say

# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n, generate the nth sequence.
# 
# Note: The sequence of integers will be represented as a string. 

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n < 1:
            return ""
        s = '1'
        for i in range(1, n):
            count, temp = 1, ''
            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    count +=1
                else:
                    temp += '{0}{1}'.format(count, s[j-1])
                    count = 1
            temp += '{0}{1}'.format(count, s[-1])
            s = temp
        return s
