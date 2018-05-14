#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (28.75%)
# Total Accepted:    496.7K
# Total Submissions: 1.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# 
# Example
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        flag = 0
        dummy = ListNode(0)
        p = dummy
        
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + flag) % 10)
            flag = (l1.val + l2.val + flag) / 10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        
        if l2:
            while l2:
                p.next = ListNode((l2.val + flag) % 10)
                flag = (l2.val + flag) / 10
                l2 = l2.next
                p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val + flag) % 10)
                flag = (l1.val + flag) / 10
                l1 = l1.next
                p = p.next
        if flag == 1:
            p.next = ListNode(1)
        
        return dummy.next
                
        
