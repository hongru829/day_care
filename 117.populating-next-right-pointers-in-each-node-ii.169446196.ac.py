#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (33.67%)
# Total Accepted:    142.3K
# Total Submissions: 422.7K
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
# 
# 
# Example:
# 
# Given the following binary tree,
# 
# 
# ⁠    1
# ⁠  /  \
# ⁠ 2    3
# ⁠/ \    \
# 4   5    7
# 
# 
# After calling your function, the tree should look like:
# 
# 
# ⁠    1 -> NULL
# ⁠  /  \
# ⁠ 2 -> 3 -> NULL
# ⁠/ \    \
# 4-> 5 -> 7 -> NULL
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
            return root
        
        queue = [root]
        root.next = None
        while queue:
            size = len(queue)
            prevNode =  None
            for k in range(size): 
                nextNode = queue.pop(0)
                if prevNode is None:
                    prevNode = nextNode
                
                
                elif k > 0:
                    prevNode.next = nextNode
                    prevNode = nextNode
                    
                if nextNode.left:
                    queue.append(nextNode.left)
                
                if nextNode.right:
                    queue.append(nextNode.right)
                    
        
                
