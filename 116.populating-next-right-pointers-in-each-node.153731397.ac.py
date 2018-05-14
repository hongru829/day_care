#
# [116] Populating Next Right Pointers in Each Node
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (36.79%)
# Total Accepted:    174.9K
# Total Submissions: 475.6K
# Testcase Example:  '{}'
#
# Given a binary tree
# 
# 
# struct TreeLinkNode {
# ⁠ TreeLinkNode *left;
# ⁠ TreeLinkNode *right;
# ⁠ TreeLinkNode *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra
# space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the
# same level, and every parent has two children).
# 
# 
# Example:
# 
# Given the following perfect binary tree,
# 
# 
# ⁠    1
# ⁠  /  \
# ⁠ 2    3
# ⁠/ \  / \
# 4  5  6  7
# 
# 
# After calling your function, the tree should look like:
# 
# 
# ⁠    1 -> NULL
# ⁠  /  \
# ⁠ 2 -> 3 -> NULL
# ⁠/ \  / \
# 4->5->6->7 -> NULL
# 
# 
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        
        if root.right and root.next:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        
#         if not root:
#             return
#         stack = [root]
        
#         while stack:
#             size = len(stack)
#             for i in range(size):
#                 node = stack.pop(0)
#                 if i < size - 1:
#                     node.next = stack[0]
#                 else:
#                     node.next = None

#                 if node.left:
#                     stack.append(node.left)
#                 if node.right:
#                     stack.append(node.right)
            
        
