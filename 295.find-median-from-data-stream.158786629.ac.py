#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (30.16%)
# Total Accepted:    63K
# Total Submissions: 208.8K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
#
from heapq import heappush, heappop, heappushpop
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.upperHeap = [float('inf')]
        self.lowerHeap = [float('inf')]
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        upperMin = + self.upperHeap[0]
        lowerMax = - self.lowerHeap[0]
        
        if num > upperMin or (lowerMax <= num <= upperMin and len(self.upperHeap) == len(self.lowerHeap)):
            heappush(self.upperHeap, num)
        else:
            heappush(self.lowerHeap, -num)
        
        if len(self.upperHeap) - len(self.lowerHeap) > 1:
            heappush(self.lowerHeap, -heappop(self.upperHeap))
        elif len(self.lowerHeap) > len(self.upperHeap):
            heappush(self.upperHeap, -heappop(self.lowerHeap))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.upperHeap) == len(self.lowerHeap):
            upperMin = + self.upperHeap[0]
            lowerMax = -self.lowerHeap[0]
            return (float(upperMin) + float(lowerMax)) /2.0
        else:
            assert len(self.upperHeap) == len(self.lowerHeap) + 1
            return float(self.upperHeap[0])
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
