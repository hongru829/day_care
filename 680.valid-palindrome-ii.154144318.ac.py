#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (32.22%)
# Total Accepted:    29K
# Total Submissions: 90K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l = 0
        r = len(s) - 1
        c1 = 0
        c2 = 0
        while l < r:
            if s[l] != s[r]:
                c1 += 1
                l += 1
            else:
                l += 1
                r -= 1
        
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                c2 += 1
                r -= 1
            else:
                l += 1
                r -= 1
        
        return c1 < 2 or c2 < 2
                
