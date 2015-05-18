#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-18 21:16:40
# Title      :  28 implement strstr

# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Update (2014-11-02):
#     The signature of the function had been updated to return the index instead of the pointer. If you still see your function signature returns a char * or String, please click the reload button to reset your code definition.

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        m, n = len(haystack), len(needle)
        for i in range(m):
            haystackIndex = i
            needleIndex = 0
            while needleIndex < n:
                if haystack[haystackIndex] != needle[needleIndex]:
                    break
                else:
                    haystackIndex += 1
                    if haystackIndex == m and needleIndex != n - 1:
                        return -1
                    needleIndex += 1

                if needleIndex == n:
                    return i
        return -1
