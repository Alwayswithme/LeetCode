#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-05 11:07:08
# Title      :  9 palindrome number

# 
# Determine whether an integer is a palindrome. Do this without extra space.
# 
# click to show spoilers.
# Some hints:
# 
# Could negative integers be palindromes? (ie, -1)
# 
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# 
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
# 
# There is a more generic way of solving this problem.

class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        sum = 0
        while x > sum:
            sum = sum * 10 + x % 10
            x /= 10
        return x == sum or x == sum / 10
