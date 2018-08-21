#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (40.15%)
# Total Accepted:    57.8K
# Total Submissions: 143.9K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
# 
# Find the number of paths that sum to a given value.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
# 
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
# 
# Example:
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# Return 3. The paths that sum to 8 are:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
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
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        res = 0
        while queue:
            size = len(queue)
            for k in range(size):
                nextNode = queue.pop(0)
                res += self.helper(nextNode, sum)
                
                if nextNode.left:
                    queue.append(nextNode.left)
                if nextNode.right:
                    queue.append(nextNode.right)
        return res
                
    def helper(self, root, target):
        res = 0
        if root is None:
            return 0
        if target == root.val:
            res += 1
        res += self.helper(root.left, target - root.val)
        res += self.helper(root.right, target - root.val)
        return res
        
        
            
            
        
