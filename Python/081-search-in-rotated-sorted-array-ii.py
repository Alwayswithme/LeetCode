#!/bin/python
#
# Author     :  Ye Jinchang
# Date       :  2015-08-26 01:16:25
# Title      :  081 search in rotated sorted array ii

# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
# Write a function to determine if a given target is in the array.

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + r >> 1
            if target == nums[m]:
                return True
            if ((nums[m] < nums[r] and target > nums[m] and target <= nums[r])
                    or (nums[m] > nums[r] and (target < nums[l] or target >= nums[m]))):
                l = m + 1
            elif ((nums[m] < nums[r] and (target <= nums[m] or target > nums[r]))
                    and (nums[m] > nums[r] and target >= nums[l] and target < nums[m])):
                r = m - 1
            else:
                r -= 1
        return False
