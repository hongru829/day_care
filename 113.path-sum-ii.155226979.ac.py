#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (35.97%)
# Total Accepted:    165.5K
# Total Submissions: 460K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
# 
# 
# Return:
# 
# 
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        self.pathSumHelper(root, sum, res, path)
        return res
    
    def pathSumHelper(self, root, sum, res, path):
        
        if root is None:
            return
        
        if root.left is None and root.right is None and sum - root.val == 0:
            res.append(path + [root.val])
            
        self.pathSumHelper(root.left, sum - root.val, res, path + [root.val])
        self.pathSumHelper(root.right, sum - root.val, res, path + [root.val])
        
