#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (36.09%)
# Total Accepted:    74.2K
# Total Submissions: 205.6K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
# 
# Note: The input string may contain letters other than the parentheses ( and
# ).
# 
# Example 1:
# 
# 
# Input: "()())()"
# Output: ["()()()", "(())()"]
# 
# 
# Example 2:
# 
# 
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
# 
# 
# Example 3:
# 
# 
# Input: ")("
# Output: [""]
# 
# 
#

import collections
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        queue = collections.deque([s])
        visited = set()
        
        visited.add(s)
        isResultContained = False
        result = []
        
        while queue:
            size = len(queue)
            for k in range(size):
                queueStr = queue.pop()
                if self.check_isValid(queueStr):
                    # print queueStr
                    isResultContained = True
                    result.append(queueStr)
                if isResultContained:
                    break
                for i in range(len(queueStr)):
                    if queueStr[i] == "(" or queueStr[i] == ")":
                        nextStr = queueStr[:i] + queueStr[i+1:]
                        if nextStr not in visited:
                            queue.appendleft(nextStr)
                            visited.add(nextStr)
        if len(result) == 0:
            return [""]
        else:
            return result
                    
    def check_isValid(self, s):
        counter = 0
        for i in range(len(s)):
            if counter < 0:
                return False
            if s[i] == '(':
                counter += 1
            elif s[i] == ')':
                counter -= 1
        return counter == 0
                
        
