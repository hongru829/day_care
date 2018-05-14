#
# [44] Wildcard Matching
#
# https://leetcode.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (21.08%)
# Total Accepted:    124.8K
# Total Submissions: 591.9K
# Testcase Example:  '"aa"\n"a"'
#
# Given an input string (s) and a pattern (p), implement wildcard pattern
# matching with support for '?' and '*'.
# 
# 
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# 
# 
# The matching should cover the entire input string (not partial).
# 
# Note:
# 
# 
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like
# ? or *.
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
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not
# match 'b'.
# 
# 
# Example 4:
# 
# 
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*'
# matches the substring "dce".
# 
# 
# Example 5:
# 
# 
# Input:
# s = "acdcb"
# p = "a*c?b"
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
        res = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        res[0][0] = True
        
        for i in range(1, len(p) + 1):
            if p[i-1] == '*':
                res[0][i] = res[0][i - 1]
            else:
                res[0][i] = False
        
        for i in range(1, len(s) + 1):
            res[i][0] = False
            
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    res[i][j] = res[i-1][j-1]
                elif p[j-1] == '*':
                    res[i][j] = res[i-1][j] or res[i][j-1]
                else:
                    res[i][j] = False
        return res[len(s)][len(p)]
    
        
