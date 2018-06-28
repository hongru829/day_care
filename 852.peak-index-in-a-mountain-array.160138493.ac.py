#
# [882] Peak Index in a Mountain Array
#
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
#
# algorithms
# Easy (69.46%)
# Total Accepted:    8.4K
# Total Submissions: 12.2K
# Testcase Example:  '[0,1,0]'
#
# Let's call an array A a mountain if the following properties hold:
# 
# 
# A.length >= 3
# There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] <
# A[i] > A[i+1] > ... > A[A.length - 1]
# 
# 
# Given an array that is definitely a mountain, return any i such that A[0] <
# A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
# 
# Example 1:
# 
# 
# Input: [0,1,0]
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: [0,2,1,0]
# Output: 1
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10^6
# A is a mountain, as defined above.
# 
# 
#
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(A) - 1
        
        while left + 1 < right:
            
            mid = (left + right) / 2
            
            # 之前写 left = mid + 1 这个test case 过不了 [24,69,100,99,79,78,67,36,26,19]
            if A[mid] < A[mid + 1]:
                left = mid
            
            else:
                right = mid

        if A[left] > A[right]:
            return left
        if A[left] < A[right]:
            return right
