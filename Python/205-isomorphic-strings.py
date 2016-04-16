#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2016-04-16 12:08:48
# Title      :  205 ismorphic strings


# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.
#
# For example,
# Given "egg", "add", return true.
#
# Given "foo", "bar", return false.
#
# Given "paper", "title", return true.
#
# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        hash = {}

        for i in range(len(s)):
            if s[i] in hash:
                if not hash[s[i]] == t[i]:
                    return False
            else:
                if t[i] in hash.values():
                    return False
                hash[s[i]] = t[i]

        return True
