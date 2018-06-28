#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (58.26%)
# Total Accepted:    86.5K
# Total Submissions: 148.4K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water. Grid cells are connected
# horizontally/vertically (not diagonally). The grid is completely surrounded
# by water, and there is exactly one island (i.e., one or more connected land
# cells). The island doesn't have "lakes" (water inside that isn't connected to
# the water around the island). One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
# 
# Example:
# 
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
#
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # maximum area is the number of 1 * 4 
        # 从图里面看 如果有相邻的1 对面积的贡献就要减去1,
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        neighbor = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    if i > 0 and grid[i-1][j]:
                        neighbor += 1
                    if i < m - 1 and grid[i + 1][j]:
                        neighbor += 1
                    if j > 0 and grid[i][j - 1]:
                        neighbor += 1
                    if j < n - 1 and grid[i][j + 1]:
                        neighbor += 1
        return count * 4 - neighbor
