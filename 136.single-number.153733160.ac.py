#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (55.66%)
# Total Accepted:    301.4K
# Total Submissions: 541.5K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         dic = {}
        
#         for i in range(len(nums)):
#             if nums[i] in dic:
#                 dic[nums[i]] += 1
#             else:
#                 dic[nums[i]] = 1
        
#         for i in range(len(nums)):
#             if dic[nums[i]] == 1:
#                 return nums[i]
        return 2*sum(set(nums)) - sum(nums)
        
