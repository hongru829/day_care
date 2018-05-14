#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (43.34%)
# Total Accepted:    64.5K
# Total Submissions: 148.8K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, implement an iterator to flatten it.
# 
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
# 
# Example 1:
# Given the list [[1,1],2,[1,1]],
# 
# By calling next repeatedly until hasNext returns false, the order of elements
# returned by next should be: [1,1,2,1,1].
# 
# 
# 
# Example 2:
# Given the list [1,[4,[6]]],
# 
# By calling next repeatedly until hasNext returns false, the order of elements
# returned by next should be: [1,4,6].
# 
# 
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.s = nestedList[:]
        

    def next(self):
        """
        :rtype: int
        """
        return self.s.pop(0).getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.s and not self.s[0].isInteger():
            self.s = self.s.pop(0).getList() + self.s
        
        if self.s and self.s[0].isInteger():
            return True
        
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
