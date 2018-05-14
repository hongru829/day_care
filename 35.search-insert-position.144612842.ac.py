#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.04%)
# Total Accepted:    257.4K
# Total Submissions: 642.8K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end)/2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                end = mid - 1
            
            elif nums[mid] < target:
                start = mid + 1
        
        if nums[start] >= target:
            return start
        elif nums[start] < target and target <= nums[end]:
            return end
        if nums[end] < target:
            return end + 1
    
