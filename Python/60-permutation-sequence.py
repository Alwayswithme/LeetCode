#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-06-18 15:33:08
# Title      :  60 permutation sequence

# The set [1,2,3,…,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):
# 
#     "123"
#     "132"
#     "213"
#     "231"
#     "312"
#     "321"
# 
# Given n and k, return the kth permutation sequence.
# 
# Note: Given n will be between 1 and 9 inclusive.

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        nums, result = [i + 1 for i in range(n)], ''
        fac = math.factorial(n)
        while n > 0:
            fac /= n
            index = (k - 1) / fac
            result += str(nums.pop(index))
            n -= 1
            k %= fac

        return result
