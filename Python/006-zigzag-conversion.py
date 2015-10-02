#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-24 10:48:18
# Title      :  #6 zigzag conversion

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a number of rows:
# 
# string convert(string text, int nRows);
# 
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR". 
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s

        index = 0
        step = 1
        lines=['' for i in range(numRows)]
        for i in s:
            lines[index] += i
            index += step
            
            if (index == 0) or (index == numRows - 1):
                step *= -1
        return "".join(lines)
