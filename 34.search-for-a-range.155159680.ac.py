#
# [34] Search for a Range
#
# https://leetcode.com/problems/search-for-a-range/description/
#
# algorithms
# Medium (31.68%)
# Total Accepted:    193.3K
# Total Submissions: 610.1K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or len(nums) == 0:
            return [-1, -1]
        left = self.searchLeftBoundry(nums, target)
        right = self.searchRightBoundry(nums, target)
        return [left, right]
    
    def searchLeftBoundry(self, nums, target):
        
        left = 0
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] < target:
                left = mid
            elif nums[mid] >= target:
                right = mid
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
        
    def searchRightBoundry(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) / 2
            if nums[mid] <= target:
                left = mid
            elif nums[mid] > target:
                right = mid
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1
                    
                
        
