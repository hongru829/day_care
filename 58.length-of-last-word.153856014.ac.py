#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.07%)
# Total Accepted:    191.9K
# Total Submissions: 598.4K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a character sequence consists of non-space
# characters only.
# 
# Example:
# 
# Input: "Hello World"
# Output: 5
# 
# 
#
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strs = s.lstrip(' ').rstrip(' ').split(' ')
        return len(strs[-1])
        
