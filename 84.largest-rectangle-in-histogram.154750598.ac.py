#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (27.78%)
# Total Accepted:    119.4K
# Total Submissions: 429.9K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 时间复杂度是 o(2n) 每一个元素只遍历了 2 遍，
        # 只要刚来的元素要比栈顶元素大的话, 不需要入栈， 只有刚来的元素比栈顶元素要小的话才去计算，主要此时此刻
        # 高度和宽度要分开，计算高度的时候, 把元素从栈里面给pop出来了
        # 所以for循环里面的元素 并没有全部进入while循环
        
        res = 0
        stack = []
        for i in range(len(heights) + 1):
            height = heights[i] if i != len(heights) else 0
            while stack and height <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1 if stack else i
                res = max(res, h*w)
            stack.append(i)
        return res
        
