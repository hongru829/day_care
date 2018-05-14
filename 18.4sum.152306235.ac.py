#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (27.65%)
# Total Accepted:    157.7K
# Total Submissions: 570.3K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        for i in xrange(len(nums) - 3):
            if i and nums[i] == nums[i-1]:
                continue
            
            for j in xrange(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                sum = target - nums[i] - nums[j]
                
                left, right = j + 1, len(nums) - 1
                
                while left < right:
                    if nums[left] + nums[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    
                    else:
                        left += 1
        return res
            
            

