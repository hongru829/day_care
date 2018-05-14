#
# [10] Regular Expression Matching
#
# https://leetcode.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.34%)
# Total Accepted:    199.2K
# Total Submissions: 818.6K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement regular expression
# matching with support for '.' and '*'.
# 
# 
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# . or *.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# 
# 
# Example 2:
# 
# 
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore,
# by repeating 'a' once, it becomes "aa".
# 
# 
# Example 3:
# 
# 
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# 
# 
# Example 4:
# 
# 
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore
# it matches "aab".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
# 
# 
#
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ns, np = len(s), len(p)
        dp = [[False] * (ns + 1) for _ in range(np + 1)]
        print dp
        
        dp[0][0] = True
        
        for i in range(np):
            for j in range(ns):
                if p[i] != '*':
                    if p[i] == s[j] or p[i] == '.':
                        dp[i+1][j+1] = dp[i][j]
                    else:
                        dp[i+1][j+1] = False
                else:
                    dp[i+1][j+1] = dp[i-1][j+1]
                    if p[i-1] == s[j] or p[i-1] == '.':
                        dp[i+1][j+1] = dp[i+1][j]|dp[i+1][j+1]
                        
        return dp[-1][-1]
