#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (41.57%)
# Total Accepted:    159.9K
# Total Submissions: 384.6K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        
        return self.contructPaths(root, str(root.val), [])
    
    def contructPaths(self, root, p, paths):
        if root.left == None and root.right == None:
            paths.append(p)
        
        if root.left:
            paths = self.contructPaths(root.left, p + "->" + str(root.left.val), paths)
        
        if root.right:
            paths = self.contructPaths(root.right, p + "->" + str(root.right.val), paths)
            
        return paths
    
    
