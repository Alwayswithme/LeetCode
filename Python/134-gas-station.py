#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-19 16:22:01
# Title      :  134 gas station

#  There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
# 
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
# 
# Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.
# 
# Note:
# The solution is guaranteed to be unique. 

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        startIndex, sum, total = -1, 0, 0
        for i, g in enumerate(gas):
            diff = g - cost[i]
            sum += diff
            total += diff
            if sum < 0:
                sum = 0
                startIndex = i
        return startIndex + 1 if total >= 0 else -1
