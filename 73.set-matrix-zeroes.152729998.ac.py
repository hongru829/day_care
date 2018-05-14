#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (36.67%)
# Total Accepted:    140.7K
# Total Submissions: 383.7K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        index_i = []
        index_j = []
        #Collectting the index of i and j where they are 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    index_i.append(i)
                    index_j.append(j)
        #again looping and setting all 0 to rows
        for i in range(len(matrix)):
            if i in index_i:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        
        #Looping and setting all zeros to column
        for j in range(len(matrix[0])):
            for j in index_j:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
