#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (38.95%)
# Total Accepted:    127.2K
# Total Submissions: 326.5K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# 
# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is
# 4. Note that there may be more than one LIS combination, it is only necessary
# for you to return the length.
# 
# 
# Your algorithm should run in O(n2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity? 
# 
# Credits:Special thanks to @pbrother for adding this problem and creating all
# test cases.
#
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp, ans = [1] * len(nums), 1
        for i in range(1, len(nums)):
            dp[i] = max([dp[j] + 1 for j in range(i) if nums[i] > nums[j]] + [1])
            ans = max(ans, dp[i])
        return ans
    
        
