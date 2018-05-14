#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (30.12%)
# Total Accepted:    133.8K
# Total Submissions: 444.2K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, head1, head2):
        if head1 == None: 
            return head2
        if head2 == None:
            return head1
        dummy = ListNode(0)
        p = dummy
        
        while head1 and head2:
            if head1.val <= head2.val:
                p.next = head1
                head1 = head1.next
                p = p.next
            else:
                p.next = head2
                head2 = head2.next
                p = p.next
        
        if head1 == None:
            p.next = head2
        
        if head2 == None:
            p.next = head1
        
        return dummy.next
            
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        head1 = head
        head2 = slow.next
        slow.next = None
        head1 = self.sortList(head1)
        head2 = self.sortList(head2)
        head = self.merge(head1, head2)
        return head
        
        
