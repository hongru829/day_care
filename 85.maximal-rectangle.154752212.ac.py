#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (29.85%)
# Total Accepted:    87.2K
# Total Submissions: 292.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
# 
# 
#
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix[0])
        
        heights = [0] * (n+1)
        
        ans = 0
        #calculate each row
        
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            stack = []
            
            for i in range(n+1):
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1] if stack else i
                    ans = max(ans, h*w)
                stack.append(i)
        return ans
        
