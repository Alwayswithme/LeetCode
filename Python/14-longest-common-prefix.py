#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-07 16:10:55
# Title      :  14 longest common prefix

# Write a function to find the longest common prefix string amongst an array of strings. 


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        longest = strs[0]
        for str in strs[1:]:
            i = 0
            while i < len(str) and i < len(longest) and str[i] == longest[i]:
                i += 1
            longest = longest[:i]
        return longest
