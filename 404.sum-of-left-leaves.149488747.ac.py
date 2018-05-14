#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (47.61%)
# Total Accepted:    87.4K
# Total Submissions: 183.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumOfLeftLeavesHelper(root, is_left):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return root.val if is_left else 0
            
            return sumOfLeftLeavesHelper(root.left, True) + \
                    sumOfLeftLeavesHelper(root.right, False)
        
        return sumOfLeftLeavesHelper(root, False)
        
