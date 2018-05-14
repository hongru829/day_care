#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (25.81%)
# Total Accepted:    156.4K
# Total Submissions: 606K
# Testcase Example:  '{}'
#
# 
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# 
# 
# Return a deep copy of the list.
# 
#
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dummy = RandomListNode(0)
        current, prev, copy = head, dummy, {}

        while current:
            copyNode = RandomListNode(current.label)
            copy[current] = copyNode
            prev.next = copyNode
            prev, current = prev.next, current.next
        
        current = head
        
        while current:
            if current.random:
                copy[current].random = copy[current.random]
            current = current.next
                
        return dummy.next
