#
# [830] Largest Triangle Area
#
# https://leetcode.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (53.02%)
# Total Accepted:    5.8K
# Total Submissions: 11K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# You have a list of points in the plane. Return the area of the largest
# triangle that can be formed by any 3 of the points.
# 
# 
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the
# largest.
# 
# 
# 
# 
# Notes: 
# 
# 
# 3 <= points.length <= 50.
# No points will be duplicated.
# -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.
# 
# 
# 
#
import math
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    a = self.euclideanDistance(points[i], points[j])
                    b = self.euclideanDistance(points[j], points[k])
                    c = self.euclideanDistance(points[k], points[i])
                    
                    if self.isValidTriangle(a, b, c):
                        S = (a + b + c) / 2
                        max_area = max(max_area, math.sqrt(S*(S-a)*(S-b)*(S-c)))
        return max_area
                    
    
    
    def euclideanDistance(self, p1, p2):
        x = p1[0] - p2[0]
        y = p1[1] - p2[1]
        return math.sqrt(x*x + y*y)
    
    def isValidTriangle(self, a, b ,c):
        return a + b > c and b + c > a and c + a > b
        
