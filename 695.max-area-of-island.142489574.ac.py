#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Easy (51.86%)
# Total Accepted:    28.4K
# Total Submissions: 54.8K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)
# 
# Example 1:
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6.
# 
# Note the answer is not 11, because the island must be connected
# 4-directionally.
# 
# 
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# 
# Note:
# The length of each dimension in the given grid does not exceed 50.
# 
#
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_size = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j, size):
            if not (0 <= i < rows and 0 <=j < cols) or grid[i][j] in (-1, 0):
                return
            size[0] += 1
            grid[i][j] = -1
            for direction in ((0,1), (1,0), (-1,0), (0,-1)):
                dfs( i + direction[0], j + direction[1], size)
                
        for i in range(rows):
            for j in range(cols):
                size = [0]
                dfs(i, j, size)
                max_size = max(max_size, size[0])
        return max_size
        
