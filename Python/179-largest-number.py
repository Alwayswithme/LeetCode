#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-11-30 15:18:34
# Title      :  179 largest number


# Given a list of non negative integers, arrange them such that they form the largest number.
# 
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
# 
# Note: The result may be very large, so you need to return a string instead of an integer.
# 
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
# 
# Subscribe to see which companies asked this question


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        strs = map(str, nums)
        strs.sort(key=cmp_to_key(lambda x,y: int(y+x)-int(x+y)))
        result = ''.join(strs).lstrip('0')
        return result or '0'

