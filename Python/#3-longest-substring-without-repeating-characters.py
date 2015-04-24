#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-24 12:27:14
# Title      :  #3 longest substring without repeating characters

# Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        sLen = len(s)
        if sLen == 0 or sLen == 1:
            return sLen

        longest = 0
        slow = 0
        fast = 0
        hashSet = set()
        while fast < sLen:
            char = s[fast]
            if char in hashSet:
                longest = max(fast - slow, longest)
                while s[slow] != char:
                    hashSet.remove(s[slow])
                    slow += 1
                slow += 1
            else:
                hashSet.add(char)
            fast += 1
        return max(fast - slow, longest)
