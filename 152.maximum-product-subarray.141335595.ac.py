#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (26.84%)
# Total Accepted:    140.5K
# Total Submissions: 523.5K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        min_tmp = nums[0]
        max_tmp = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            a = nums[i] * min_tmp
            b = nums[i] * max_tmp
            c = nums[i] 
            max_tmp = max(max(a,b),c)
            min_tmp = min(min(a,b),c)
            result = max_tmp if max_tmp > result else result
        return result
        
