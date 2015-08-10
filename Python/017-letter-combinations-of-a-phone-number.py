#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-14 23:14:21
# Title      :  16 letter combinations of a phone number

# Given a digit string, return all possible letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want. 

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        comb = []
        if not digits:
            return comb
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz", "0": " "}
        self.add(comb, mapping, digits, "")
        return comb
        
    def add(self, comb, mapping, digit, concat):
        if not digit:
            comb.append(concat)
            return
        now = digit[:1]
        rem = digit[1:]
        
        letters = mapping[now]
        for i in letters:
            newConcat = concat + i
            self.add(comb, mapping, rem, newConcat)
