#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (28.45%)
# Total Accepted:    225.2K
# Total Submissions: 791.3K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for nodes in lists:
            if nodes:
                heap.append((nodes.val, nodes))
        heapq.heapify(heap)
        
        head = ListNode(0)
        cur = head
        while heap:
            pop = heapq.heappop(heap);
            cur.next = ListNode(pop[0])
            cur = cur.next
            if pop[1].next != None:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
        
        return head.next
            
