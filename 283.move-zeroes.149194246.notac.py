#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (51.66%)
# Total Accepted:    291K
# Total Submissions: 563.3K
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
# 
#
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 这样的话就改变了原来的顺序了
        # j = len(nums) - 1
        # for i in range(len(nums)):
        #     if nums[i] == 0 and i < j:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         j -= 1
        
        zero = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[zero], nums[i]
                zero += 1
        
