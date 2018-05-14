#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (21.80%)
# Total Accepted:    325.4K
# Total Submissions: 1.5M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                if sum < 0:
                    left += 1
                
                if sum > 0:
                    right -= 1
        
        return list(res)
                
        
