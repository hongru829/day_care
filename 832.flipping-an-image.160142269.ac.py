#
# [861] Flipping an Image
#
# https://leetcode.com/problems/flipping-an-image/description/
#
# algorithms
# Easy (69.97%)
# Total Accepted:    17.2K
# Total Submissions: 24.5K
# Testcase Example:  '[[1,1,0],[1,0,1],[0,0,0]]'
#
# Given a binary matrix A, we want to flip the image horizontally, then invert
# it, and return the resulting image.
# 
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
# 
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced
# by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].
# 
# Example 1:
# 
# 
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# 
# 
# Example 2:
# 
# 
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row:
# [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 
# 
# Notes:
# 
# 
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1
# 
#
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        
        for i in range(m):
            
            j = len(A[i]) - 1
            k = 0
            
            while k <= j:
                temp = A[i][k]
                A[i][k] = A[i][j] ^ 1
                A[i][j] = temp ^ 1
                k += 1
                j -= 1
        return A
            
