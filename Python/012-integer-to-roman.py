#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-05 11:27:23
# Title      :  12 integer to roman

# Given an integer, convert it to a roman numeral.
# 
# Input is guaranteed to be within the range from 1 to 3999.

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        res = ''
        for i in range(len(integers)):
            num, remainder = divmod(num, integers[i])
            res+=num*numerals[i]
            num = remainder

        return res
