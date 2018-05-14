#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.24%)
# Total Accepted:    136.8K
# Total Submissions: 424.1K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for p in range(n)] for q in range(m)]
        
        if m == 1 and n == 1:
            if obstacleGrid[0][0] == 1:
                return 0
            else:
                return 1
        
        for i in xrange(0, m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                res[i][0] = 1
        for j in xrange(0, n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                res[0][j] = 1
        
        if m > 1 and n > 1:
            for i in xrange(1, m):
                for j in xrange(1, n):
                    if obstacleGrid[i][j] == 1:
                        res[i][j] = 0
                    else:
                        res[i][j] = res[i-1][j] + res[i][j-1]
                    
                    
        return res[m-1][n-1]
            
        
