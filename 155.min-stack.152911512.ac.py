#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (31.52%)
# Total Accepted:    188.6K
# Total Submissions: 598.4K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# 
# 
# pop() -- Removes the element on top of the stack.
# 
# 
# top() -- Get the top element.
# 
# 
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
#
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack1.append(x)
        if len(self.stack2) == 0 or x <= self.stack2[-1]:
            self.stack2.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        top = self.stack1[-1]
        self.stack1.pop()
        
        if top == self.stack2[-1]:
            self.stack2.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack1[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
