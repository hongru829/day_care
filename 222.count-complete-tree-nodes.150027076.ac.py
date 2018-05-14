#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (27.79%)
# Total Accepted:    78.6K
# Total Submissions: 282.6K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2h nodes inclusive at the last level h.
# 
# Example:
# 
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# Output: 6
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        left = self.getLeftHeight(root) + 1
        right = self.getRightHeight(root) + 1
        
        if left == right:
            return (2<<(left-1)) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
        
        
    def getLeftHeight(self, root):
        if root == None:
            return 0
        height = 0
        while root.left != None:
            height += 1
            root = root.left
        return height
    
    def getRightHeight(self, root):
        if root == None:
            return 0
        height = 0
        while root.right != None:
            height += 1
            root = root.right
        return height
    
        
