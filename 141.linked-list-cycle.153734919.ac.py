#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (35.01%)
# Total Accepted:    254.1K
# Total Submissions: 725.6K
# Testcase Example:  '[]\nno cycle'
#
# 
# Given a linked list, determine if it has a cycle in it.
# 
# 
# 
# Follow up:
# Can you solve it without using extra space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        
        while head is not None:
            if head in s:
                return True
            else:
                s.add(head)
            head = head.next
        
        return False
                    
        
