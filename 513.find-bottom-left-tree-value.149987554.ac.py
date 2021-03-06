#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (56.15%)
# Total Accepted:    44.3K
# Total Submissions: 78.9K
# Testcase Example:  '[2,1,3]'
#
# 
# Given a binary tree, find the leftmost value in the last row of the tree. 
# 
# 
# Example 1:
# 
# Input:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Output:
# 1
# 
# 
# 
# ⁠ Example 2: 
# 
# Input:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# Output:
# 7
# 
# 
# 
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        max_depth = 0
        queue = [(root, 1)]
        
        while queue:
            cur, level = queue.pop(0)
            
            if cur:
                if level > max_depth:
                    max_depth = level
                    ans = cur.val
                queue.append((cur.left, level + 1))
                queue.append((cur.right, level + 1))
        return ans
        
