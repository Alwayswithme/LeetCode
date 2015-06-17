#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-17 13:56:42
# Title      :  49 anagrams

# Given an array of strings, return all groups of strings that are anagrams.
# 
# Note: All inputs will be in lower-case.

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dict, results = {}, []
        for str in strs:
            key = ''.join(sorted(str))
            if key in dict:
                dict[key].append(str)
            else:
                dict[key] = [str]

        for list in dict.values():
            if len(list) > 1:
                results += list

        return results
