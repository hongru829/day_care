#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (38.91%)
# Total Accepted:    44.4K
# Total Submissions: 114.1K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# 
# Note:
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# Example 1:
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# Example 2:
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
#
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        
        if not nums or s % 2 == 1:
            return False
        
        dp = [[False for _ in range(s/2 + 1)] for _ in xrange(len(nums) + 1)]

        for i in xrange(len(nums) + 1):
            dp[i][0] = True
        
        for i in xrange(1, len(nums) + 1):
            for j in xrange(1, s/2 + 1):
                if dp[i-1][j]:
                    dp[i][j] = dp[i-1][j]
                elif (j - nums[i-1]) >= 0:
                    dp[i][j] = dp[i-1][j - nums[i-1]]
        
        if s % 2 == 0:
            return dp[len(nums)][s/2]
        else:
            return False
        
