#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.21%)
# Total Accepted:    93.6K
# Total Submissions: 615.7K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
# 
# Example 1:
# 
# 
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# 
# 
#
# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        length = len(points)
        if length < 3: return length
        res = -1
        for i in range(length):
            slope = {'inf': 0}
            samePointsNum = 1
            for j in range(length):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    slope['inf'] += 1
                elif points[i].x != points[j].x:
                    k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    if k not in slope:
                        slope[k] = 1
                    else:
                        slope[k] += 1
                else:
                    samePointsNum += 1
            res = max(res, max(slope.values()) + samePointsNum)
        return res
