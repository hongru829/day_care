#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (15.72%)
# Total Accepted:    217.5K
# Total Submissions: 1.4M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
# 
# Example:  
# 
# 
# Input: "the sky is blue",
# Output: "blue is sky the".
# 
# 
# Note:
# 
# 
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
# 
# 
# Follow up: For C programmers, try to solve it in-place in O(1) space.
# 
#
class Solution(object):
     def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        i = 0
        j = len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        res = []
        for i in range(len(s)):
            if s[i] != "":
                res.append(s[i])
                
        if len(res) == 0:
            return ""
        
        return " ".join(res)
