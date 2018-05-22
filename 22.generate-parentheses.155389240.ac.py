#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (48.40%)
# Total Accepted:    212.1K
# Total Submissions: 438.2K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.dfs(0, 0, res, "", n)
        return res
    
    def dfs(self, left, right, res, temp, n):
        
        if left < right:
            return False
        
        if left == n and right == n:
            res.append(temp)
        
        if left < n:
            self.dfs(left + 1, right, res, temp + '(', n)
        
        if right < n:
            self.dfs(left, right + 1, res, temp  + ')', n)
        
