#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (44.90%)
# Total Accepted:    22.2K
# Total Submissions: 49.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image. 
# 
# 
# Example:
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output:  [1,2,4,7,5,3,6,8,9]
# Explanation:
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
# 
#
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
    
        
        resLen = m + n - 1
        res = []
        finalres = []
        
        for i in range(resLen):
            res.append([])
        
        for i in range(m):
            for j in range(n):
                res[i + j].append(matrix[i][j])
    
        for i in range(0, m + n - 1, 2):
           res[i].reverse()
        
        
        for list in res:
            for ele in list:
                finalres.append(ele)
        
        return finalres
        
            
