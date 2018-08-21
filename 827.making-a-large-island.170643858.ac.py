#
# [854] Making A Large Island
#
# https://leetcode.com/problems/making-a-large-island/description/
#
# algorithms
# Hard (40.54%)
# Total Accepted:    4.1K
# Total Submissions: 10K
# Testcase Example:  '[[1,0],[0,1]]'
#
# In a 2D grid of 0s and 1s, we change at most one 0 to a 1.
# 
# After, what is the size of the largest island? (An island is a
# 4-directionally connected group of 1s).
# 
# Example 1:
# 
# 
# Input: [[1, 0], [0, 1]]
# Output: 3
# Explanation: Change one 0 to 1 and connect two 1s, then we get an island with
# area = 3.
# 
# 
# Example 2:
# 
# 
# Input: [[1, 1], [1, 0]]
# Output: 4
# Explanation: Change the 0 to 1 and make the island bigger, only one island
# with area = 4.
# 
# Example 3:
# 
# 
# Input: [[1, 1], [1, 1]]
# Output: 4
# Explanation: Can't change any 0 to 1, only one island with area = 4.
# 
# 
# 
# Notes:
# 
# 
# 1 <= grid.length = grid[0].length <= 50.
# 0 <= grid[i][j] <= 1.
# 
# 
# 
# 
#
class UnionFind:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.root = [i for i in range(m*n)]
        self.size = [1] * (m*n)
    
    def union(self, p1, p2):
        p1, p2 = self.getcoor(p1), self.getcoor(p2)
        root1 = self.find(p1)
        root2 = self.find(p2)
        if root1 == root2:
            return
        self.root[root2] = root1
        self.size[root1] += self.size[root2]
    
    def find(self, p):
        if isinstance(p, list):
            p = self.getcoor(p)
        while p != self.root[p]:
            p = self.root[p]
        return p
    
    def getcoor(self, p):
        i, j = p
        return self.m * i + j
    
    def getans(self, i, j, grid):
        seen = set()
        
        res = 0
        
        for di, dj in [[0,1], [1,0], [-1, 0], [0, -1]]:
            ni, nj = i + di, j + dj
            if not -1 < ni < self.m or not -1 < nj < self.n:
                continue
            if grid[ni][nj] == 0:
                continue
            rij = self.find([ni, nj])
            if rij in seen:
                continue
            seen.add(rij)
            res += self.size[rij]
        return res + 1


class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        uf = UnionFind(m, n)
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                for d in [[0, 1], [0, -1], [-1, 0], [0, -1]]:
                    x = d[0] + i
                    y = d[1] + j
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    elif grid[x][y] == 1:
                        uf.union([i, j], [x, y])
        
        print uf.root
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans = max(ans, uf.getans(i, j, grid))
        
        return ans if ans else m * n
        
