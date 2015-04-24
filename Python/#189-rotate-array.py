# Title      :  #189 rotate array
#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-04-24 10:41:29
# Title      :  #189 rotate array

# Rotate an array of n elements to the right by k steps.
# 
# For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
# 
# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# 
# [show hint]
# 
# Related problem: Reverse Words in a String II
# 
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        if (k == 0):
            return

        a = nums[:n-k][::-1]
        b = nums[n-k:][::-1]
        l = a + b
        l.reverse()
        for i in xrange(n):
            nums[i] = l[i]
