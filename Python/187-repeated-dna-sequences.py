#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-12-01 18:05:48
# Title      :  187 repeated dna sequences


#  All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
# 
# For example,
# 
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# 
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
# 
# Subscribe to see which companies asked this question

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        ret = []
        lookup = {}
        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in lookup:
                if lookup[seq]:
                    lookup[seq] = False
                    ret.append(seq)
            else:
                lookup[seq] = True
        return ret
