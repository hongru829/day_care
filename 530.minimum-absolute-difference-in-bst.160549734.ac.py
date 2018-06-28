#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (47.88%)
# Total Accepted:    39.5K
# Total Submissions: 82.5K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# 
# Example:
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note:
# There are at least two nodes in this BST.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    
    
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        self.res = float('inf')
        self.minDiffInBSTHelper(root)
        return self.res
    
    def minDiffInBSTHelper(self, root):

        if root is None:
            return
        self.minDiffInBSTHelper(root.left)
        
        if self.prev == None:
            self.prev = root.val
        else:
            self.res = min(abs(self.prev - root.val), self.res)
            self.prev = root.val
        self.minDiffInBSTHelper(root.right)

