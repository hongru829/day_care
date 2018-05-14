#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (37.18%)
# Total Accepted:    200.2K
# Total Submissions: 538.4K
# Testcase Example:  '[1,1]'
#
# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # maxArea = 0
        # for i in range(len(height)):
        #     for j in range(i+1, len(height)):
        #         maxArea = max(maxArea, min(height[i], height[j])*(j-i))
        # return maxArea
        maxArea = 0
        l = 0
        r = len(height) - 1
        
        while l < r:
            maxArea = max(maxArea, min(height[l], height[r])* (r - l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
        
