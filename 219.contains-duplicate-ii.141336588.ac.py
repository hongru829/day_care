#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (32.93%)
# Total Accepted:    144.6K
# Total Submissions: 439K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1], k = 3
# Output: true
# 
# Example 2:
# 
# 
# Input: [1,0,1,1], k = 1
# Output: true
# 
# Example 3:
# 
# 
# Input: [1,2,1], k = 0
# Output: false
# 
#
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if nums == None:
            return True
        nums_map = {}
        
        for i in range(len(nums)):
            if nums[i] in nums_map and i - nums_map[nums[i]] <= k:
                return True
            else:
                nums_map[nums[i]] = i
        return False
