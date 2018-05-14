#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (24.12%)
# Total Accepted:    242.9K
# Total Submissions: 1M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's
# value
# is 5 but its right child's value is 4.
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, leftBoundary, rightBoundary):
            
            if root == None:
                return True
            
            if leftBoundary is not None and root.val <= leftBoundary:
                return False
            
            if rightBoundary is not None and root.val >= rightBoundary:
                return False
            
            return dfs(root.left, leftBoundary, root.val) and dfs(root.right, root.val, rightBoundary)
        
        return dfs(root, None, None)
        
            
        
