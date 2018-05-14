#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (25.50%)
# Total Accepted:    184K
# Total Submissions: 721.5K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Note:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
# 
#
class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k %= n
#         self.reverse(nums, 0, n-k)
#         self,reverse(nums, n-k, n)
#         self.reverse(nums, 0, n)
        
#     def reverse(self, nums, start, end):
#         for i in range(start, (start + end) / 2):
#             nums[i], nums[start + end - i - 1] = nums[start+end-i-1],nums[i]
#     def rotate(self, nums, k):
#         n = len(nums)
#         k %= n
#         self.reverse(nums, 0, n - k)
#         self.reverse(nums, n - k, n)
#         self.reverse(nums, 0, n)

#     def reverse(self, nums, start, end):
#         for x in range(start, (start + end) / 2):
#             nums[x], nums[start + end - x - 1] = nums[start+end-x-1],nums[x]
            
            
    #second method
    def rotate(self, nums, k):
        n = len(nums)
        if k > 0 and n > 1:
            nums[:] = nums[n-k:] + nums[:n-k]
    
        
