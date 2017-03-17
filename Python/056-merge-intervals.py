#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2017-03-18 00:20:12
# Title      :  056 merge intervals

# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda i: i.start)

        start,end = intervals[0].start, intervals[0].end
        result = []
        for i in intervals[1:]:
            if i.start <= end:
                end = max(i.end, end)
            else:
                result.append(Interval(start, end))
                start, end = i.start, i.end

        result.append(Interval(start, end))
        return result
