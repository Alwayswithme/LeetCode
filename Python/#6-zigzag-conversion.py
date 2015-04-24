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

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if (nRows == 1):
            return s
        index = 0
        step = 1
        # init nRows lines
        lines=['' for i in range(nRows)]
        for i in range(len(s)):
            # append a char in current line and move to next line
            lines[index] += s[i]
            index += step
            if (index == 0) or (index == nRows - 1):
                # trun around
                step *= -1
        return "".join(lines)
