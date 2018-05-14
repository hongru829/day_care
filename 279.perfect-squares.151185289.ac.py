#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (37.79%)
# Total Accepted:    111.2K
# Total Submissions: 294.3K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
# 
#
import sys
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[n] = Min{dp[n - i*i] + 1, n - i*i >=0 && i >= 1}
        dp = [sys.maxint for _ in range(n+1)]
        dp[0] = 0
        
        for i in range(1, n+1):
            min_value = sys.maxint
            j = 1
            
            while i - j*j >= 0:
                min_value = min(min_value, dp[i - j*j] + 1);
                j += 1
                
            dp[i] = min_value
            
        return dp[n]
