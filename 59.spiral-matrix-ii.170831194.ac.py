#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (42.54%)
# Total Accepted:    109.7K
# Total Submissions: 257.8K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        def change_dir(x, y):
            return x < 0 or x == n or y < 0 or y == n or res[x][y] > 0
        
        
        if n <= 0:
            return []
        res = [[-1] * n for _ in range(n)]
        vals = range(1, n ** 2 + 1)
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        cur = 0, -1
        direction = 0
        
        for val in vals:
            x, y = cur
            dx, dy = dirs[direction]
            if change_dir(x + dx, y + dy):
                direction = (direction + 1) % 4
                dx, dy = dirs[direction]
            cur = x + dx, y + dy
            res[cur[0]][cur[1]] = val
            
        return res
        
