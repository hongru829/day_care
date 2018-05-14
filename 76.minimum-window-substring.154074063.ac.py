#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (27.00%)
# Total Accepted:    148.8K
# Total Submissions: 551K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s and not t:
            return ""
        res = ""
        dic = dict()
        
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        
        l, r = 0, 0
        
        minLength = len(s)
        
        size = len(t)
        
        while r < len(s):
            if s[r] in dic:
                if dic[s[r]] > 0:
                    size -= 1
                
                dic[s[r]] -= 1
        
            r += 1
            
            while size == 0:
                if minLength >= r - l:
                    minLength = r - l
                    res = s[l:r]
                
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        size += 1
                l += 1
        
        return res
        
        
        
