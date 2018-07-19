#
# [799] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (47.60%)
# Total Accepted:    11.2K
# Total Submissions: 23.6K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
#
# Example :
#
#
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
#
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
#
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \
# ⁠   1   3
#
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
#
#
# Note:
#
#
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def minDiffInBST(self, root):
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