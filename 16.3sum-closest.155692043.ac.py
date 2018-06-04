#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (31.90%)
# Total Accepted:    179.9K
# Total Submissions: 563.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            j, k = i+1, len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return temp
                
                if abs(temp - target) < abs(result - target):
                    result = temp
                    
                if temp < target:
                    j += 1
                
                elif temp > target:
                    k -= 1
        return result
        
