#
# [217] Contains Duplicate
#
# https://leetcode.com/problems/contains-duplicate/description/
#
# algorithms
# Easy (47.31%)
# Total Accepted:    218.3K
# Total Submissions: 461.4K
# Testcase Example:  '[1,2,3,1]'
#
# Given an array of integers, find if the array contains any duplicates.
# 
# Your function should return true if any value appears at least twice in the
# array, and it should return false if every element is distinct.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: true
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: false
# 
# Example 3:
# 
# 
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
# 
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in nums:
            if i in map:
                return True
            map[i] = True
        return False
    
#         nums.sort()
        
#         for i in xrange(0, len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False
        
        
        
        
