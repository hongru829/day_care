#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (31.91%)
# Total Accepted:    17.9K
# Total Submissions: 56K
# Testcase Example:  '[1,3,5,4,7]'
#
# 
# Given an unsorted array of integers, find the number of longest increasing
# subsequence.
# 
# 
# Example 1:
# 
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1,
# 3, 5, 7].
# 
# 
# 
# Example 2:
# 
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
# 
# 
# 
# Note:
# Length of the given array will be not exceed 2000 and the answer is
# guaranteed to be fit in 32-bit signed int.
# 
#
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dp menas in position i and include nums[i] , the length of longest increaisng subsequence
        dp = [0 for _ in range(len(nums))]
        length = [1 for _ in range(len(nums))]
        
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 == dp[i]:
                        length[i] += length[j]
                    elif dp[j] >= dp[i]:
                        length[i] = length[j]
                        dp[i] = dp[j] + 1
        
        longest = 0
        for i in range(len(dp)):
            longest = max(dp[i], longest)
        
        res = 0
        for i in range(len(length)):
            if dp[i] == longest:
                res += length[i]
        
        
        return res
            
            
    
        

         
                
                
            
    
        
