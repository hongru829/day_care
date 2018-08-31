#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (36.81%)
# Total Accepted:    177.3K
# Total Submissions: 481.7K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# Example 1:
# 
# 
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
# 
# 
#
class UnionFind(object):
    
    def __init__(self, m, n, count):
        self.m = m
        self.n = n
        self.root = [i for i in range(m * n)]
        self.size = [1] * (m * n)
        self.count = count
    
    def getCoor(self, p):
        i, j = p
        # 一定要重视 是 self.n 不是 self.m
        return self.n * i + j
    
    def find(self, p):
        p = self.getCoor(p)
        while p != self.root[p]:
            p = self.root[p]
        return p
    
    def union(self, p1, p2):
        root1 = self.find(p1)
        root2 = self.find(p2)
        if root1 == root2:
            return
        self.root[root2] = root1
        self.size[root1] += self.size[root2]
        self.count -= 1



class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0 or grid is None:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    
        uf = UnionFind(len(grid), len(grid[0]), count)
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    visited.add((i, j))
                    for dir in [[0,1], [0, -1], [-1, 0], [1, 0]]:
                        x = dir[0] + i
                        y = dir[1] + j
                        if x < 0 or x >=m or y < 0 or y >= n or (x, y) in visited:
                            continue
                        elif grid[x][y] == '1':
                            uf.union([i, j], [x, y])
        return uf.count
        
                
