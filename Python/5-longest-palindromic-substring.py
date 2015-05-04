#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-03 23:55:18
# Title      :  5 longest palindromic substring

# Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

class Solution:
    def findPalindrome(self, s, l, r):
         while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
         return s[l+1 : r]
    # @return a string
    def longestPalindrome(self, s):
        if (len(s) <= 1):
            return s
        longest = ''
        for i in xrange(len(s)):
            # odd
            result = self.findPalindrome(s, i, i)
            if (len(result) > len(longest)):
                longest = result
            # even
            result = self.findPalindrome(s, i, i+1)
            if (len(result) > len(longest)):
                longest = result
        
        return longest
