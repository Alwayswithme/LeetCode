#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-10-12 15:34:16
# Title      :  121 best time to buy and sell stock

# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices.pop(0)
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(max_profit, p - min_price)
        return max_profit
