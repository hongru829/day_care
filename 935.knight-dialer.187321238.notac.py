#
# [972] Knight Dialer
#
# https://leetcode.com/problems/knight-dialer/description/
#
# algorithms
# Medium (33.45%)
# Total Accepted:    2.5K
# Total Submissions: 7.6K
# Testcase Example:  '1'
#
# A chess knight can move as indicated in the chess diagram below:
# 
# .           
# 
# 
# 
# This time, we place our chess knight on any numbered key of a phone pad
# (indicated above), and the knight makes N-1 hops.  Each hop must be from one
# key to another numbered key.
# 
# Each time it lands on a key (including the initial placement of the knight),
# it presses the number of that key, pressing N digits total.
# 
# How many distinct numbers can you dial in this manner?
# 
# Since the answer may be large, output the answer modulo 10^9 + 7.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: 10
# 
# 
# 
# Example 2:
# 
# 
# Input: 2
# Output: 20
# 
# 
# 
# Example 3:
# 
# 
# Input: 3
# Output: 46
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 5000
# 
# 
# 
# 
#
class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """
        # dp[i][j] means that knight in the position i,has already jth steps
        dp = [[1 for _ in range(N)] for _ in range(10)]
        for j in range(1, N):
            dp[0][j] = dp[4][j-1] + dp[6][j-1]
            dp[1][j] = dp[8][j - 1] + dp[6][j-1] 
            dp[2][j] = dp[7] [j - 1] + dp[9][j-1]
            dp[3][j] = dp[8][j - 1] + dp[4][j-1]
            dp[4][j] = dp[9][j - 1] + dp[3][j-1] + dp[0][j - 1]
            dp[5][j] = 0
            dp[6][j] = dp[7][j - 1] + dp[1][j-1] + dp[0][j - 1]
            dp[7][j] = dp[2][j - 1] + dp[6][j-1]
            dp[8][j] = dp[1][j - 1] + dp[3][j-1]
            dp[9][j] = dp[4][j - 1] + dp[2][j-1]
        
        summer = 0
        for i in range(10):
            summer += dp[i][N - 1]
        return summer % (10**9 + 7)
            
        
