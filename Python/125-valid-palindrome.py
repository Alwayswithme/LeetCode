#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-12 15:55:21
# Title      :  125 valid palindrome

#  Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# 
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
# 
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# 
# For the purpose of this problem, we define empty string as valid palindrome. 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start, end = start + 1, end - 1
        return True
