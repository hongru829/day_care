#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (37.81%)
# Total Accepted:    168.2K
# Total Submissions: 444.9K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#
class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        for i in range(len(nums)):
            left[i] = max(nums[i], left[i-1])
        
        right[len(nums) - 1] = nums[len(nums) - 1]
        
        for i in range(len(nums)-2, -1, -1):
            right[i] = max(nums[i], right[i+1])
        
        trapWater = 0
        
        for i in range(len(nums)):
            bit = min(left[i], right[i]) - nums[i]
            
            if bit > 0:
                trapWater += bit
        
        return trapWater
