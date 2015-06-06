class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.powRecur(x, -n)
        return self.powRecur(x, n)
    
    def powRecur(self, x, n):
        if n == 0:
            return 1
        if n & 1 != 1:
            # even
            return self.powRecur(x * x, n / 2)
        return x * self.powRecur(x * x, n / 2)
