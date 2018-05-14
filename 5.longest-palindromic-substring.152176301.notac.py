#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.39%)
# Total Accepted:    317.8K
# Total Submissions: 1.3M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        slen = len(s)
        res = None
        
        dp = [[False for _ in range(slen)] for _ in range(slen)]
        
        for i in range(slen-1, -1, -1):
            for j in range(i, slen):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i+1][j-1])
                
                if dp[i][j] and (res == None or j - i + 1 > len(res)):
                    res = s[i:j+1]
                    
        return res
