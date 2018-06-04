#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (27.55%)
# Total Accepted:    147.9K
# Total Submissions: 537K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        
        up = 0; left = 0
        
        down =  len(matrix) - 1
        right = len(matrix[0]) - 1
        # 0 go tight 1, go down, 2 go left, 3: go up
        direct = 0
        res = []
        
        while True:
            if direct == 0:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
            
            if direct == 1:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
            
            if direct == 2:
                for i in range(right, left-1, -1):
                    res.append(matrix[down][i])
                down -= 1
            
            if direct == 3:
                for i in range(down, up-1, -1):
                    res.append(matrix[i][left])
                left += 1
                
            if up > down or left > right:
                return res
            
            direct = (direct + 1) % 4
