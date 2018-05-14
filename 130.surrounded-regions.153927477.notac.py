#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (19.81%)
# Total Accepted:    102.9K
# Total Submissions: 519.4K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
# 
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
# 
# Example:
# 
# 
# X X X X
# X O O X
# X X O X
# X O X X
# 
# 
# After running your function, the board should be:
# 
# 
# X X X X
# X X X X
# X X X X
# X O X X
# 
# 
# Explanation:
# 
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
# 
#
class UnionFind(object):
    
    def __init__(self, borad, m, n):
        self.parent = [-1] * (m*n+1)
        self.rank = [0]* (m*n + 1)
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O':
                    self.parent[i*n + j] = i*n + j
    
    def add(self, i):
        self.parent[i] = i
        self.rank[i] = 0
    
    def is_connected(self, i, j):
        return self.find(i) == self.find(j)

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        returun self.parent[i]
    
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            

class Solution(object):
    
    def is_valid(self, board, r, c):
        m, n = len(board), len(board[0])
        
        if r < 0 or c < 0 or r >=m or c >=n:
            return False
        
        return True
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
        
        for i in xrange(m):
            if board[i][0] == 'O':
                self.dfs(board, i, 0)
            
            if board[i][n-1] == 'O':
                self.dfs(board, i, n - 1)
            
        
        for j in xrange(n):
            
            if board[0][j] == 'O' :
                self.dfs(board, 0, j)
            
            if board[m-1][j] == 'O':
                self.dfs(borad, m-1, j)
                
        
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == '#':
                    board[i][j] == 'O'
                else:
                    board[i][j] = 'X'
        
        def dfs(self, board, r, c):
            board[r][c] = '#'
            directions = [(0,1), (0, -1), (-1, 0), (1, 0)]
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                
                if self.is_valid(board, nr, nc) and board[nr][nc] == '0':
                    self.dfs(board, nr, nc)
        
