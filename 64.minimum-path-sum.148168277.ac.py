#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (41.15%)
# Total Accepted:    151.2K
# Total Submissions: 367.3K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 
        m, n = len(grid), len(grid[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        
        res[0][0] = grid[0][0]
        for i in xrange(1, m):
            res[i][0] = res[i-1][0] + grid[i][0]
        for j in xrange(1, n):
            res[0][j] = res[0][j-1] + grid[0][j]
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        
        return res[-1][-1]
        
