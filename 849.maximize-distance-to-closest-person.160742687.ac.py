#
# [879] Maximize Distance to Closest Person
#
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Easy (39.16%)
# Total Accepted:    5.1K
# Total Submissions: 13K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# In a row of seats, 1 represents a person sitting in that seat, and 0
# represents that the seat is empty. 
# 
# There is at least one empty seat, and at least one person sitting.
# 
# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized. 
# 
# Return that maximum distance to closest person.
# 
# 
# Example 1:
# 
# 
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has
# distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# 
# Example 2:
# 
# 
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# 
# 
# Note:
# 
# 
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
# 
# 
# 
# 
#
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        N = len(seats)
        left, right = [N]*N, [N]*N
        
        for i in xrange(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1
        
        for i in xrange(N-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N-1:
                right[i] = right[i+1] + 1
        return max(min(left[i],right[i])
                  for i, seat in enumerate(seats) if not seat)

