#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (45.59%)
# Total Accepted:    61.2K
# Total Submissions: 134.2K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.
#
from heapq import heappush, heappop
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        kth_smallest = 0
        min_heap = []
        
        def push(i, j):
            if len(matrix) > len(matrix[0]):
                if i < len(matrix[0]) and j < len(matrix):
                    heappush(min_heap, (matrix[j][i], i, j))
            else:
                if i < len(matrix) and j < len(matrix[0]):
                    heappush(min_heap, (matrix[i][j], i, j))
        
        push(0, 0)
        
        while min_heap and k > 0:
            kth_smallest, i, j = heappop(min_heap)
            push(i , j + 1)
            if j == 0:
                push(i+1, 0)
            k -= 1
            
        return kth_smallest
            
 

        
        
        
