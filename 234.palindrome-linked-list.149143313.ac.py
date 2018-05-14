#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (33.57%)
# Total Accepted:    160.3K
# Total Submissions: 477.5K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow = fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        slow = slow.next
        slow = self.reverseList(slow)
        
        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next
        return True
        
        
    def reverseList(self, head):
        prev = None
        cur = head
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
            
