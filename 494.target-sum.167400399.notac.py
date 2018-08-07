#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (44.05%)
# Total Accepted:    61.5K
# Total Submissions: 139.7K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        def dfs(nums, S, calSum, count, index, strs):
            
            if calSum == S and index == len(nums):
                # print strs
                # print index
                count[0] += 1
                return
            
            if index == len(nums):
                return
            dfs(nums, S, calSum + nums[index], count, index + 1, strs + '+' + str(nums[index]))
            dfs(nums, S, calSum - nums[index], count, index + 1, strs + '-' + str(nums[index]))
        
        count = [0]
        dfs(nums, S, 0, count, 0, "")
        return count[0]
            
                
            
        
