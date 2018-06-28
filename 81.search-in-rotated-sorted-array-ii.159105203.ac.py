#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.58%)
# Total Accepted:    125.1K
# Total Submissions: 384.1K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if nums is None or len(nums) == 0:
            return False
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) / 2
            
            if target == nums[mid]:
                return True
            
            # 4,5,6,7,0,1,2
            elif nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            # 6 7 0 1 2 3 4
            elif nums[mid] < nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                right -= 1
        
        if nums[left] == target:
            return True
        if nums[right] == target:
            return True
        
        return False    
