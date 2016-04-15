#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2016-04-13 23:05:23
# Title      :  204 count primes

# Description:
#
# Count the number of prime numbers less than a non-negative number, n.


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        is_prime = [True] * n

        for i in range(2, int(n ** 0.5 + 1)):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        return count
