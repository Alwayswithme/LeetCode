#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-05-19 15:41:24
# Title      :  11 container with most water

# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container. 

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        n = len(height)
        area = 0
        if n < 2:
            return area
        start, end = 0, n-1
        
        while start < end:
            area = max(area, (end - start) * min(height[start], height[end]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return area
