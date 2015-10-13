#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-22 17:16:16
# Title      :  139 word break

#  Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# 
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# 
# Return true because "leetcode" can be segmented as "leet code". 

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        result = [False for i in range(len(s) + 1)]
        result[0] = True
        for i in range(len(s)):
            splitStr = s[:i + 1]
            for j in range(i + 1):
                if result[j] and splitStr in wordDict:
                    result[i + 1] = True
                    break
                splitStr = splitStr[1:]
        return result[-1]
