#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (27.28%)
# Total Accepted:    128.2K
# Total Submissions: 469.9K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            l = r = 0
            ls = rs = None
            
            if node.left:
                l, ls = dfs(node.left)
                l = max(l, 0)
            
            if node.right:
                r, rs = dfs(node.right)
                r = max(r, 0)
                
            return node.val + max(l, r), max(node.val + l + r, ls, rs)
        
        if root:
            return dfs(root)[1]
        return 0
                
