#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (24.67%)
# Total Accepted:    114.9K
# Total Submissions: 465.5K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.res = []
        self.dfs(s, wordDict, '')
        return self.res
        
    
    
    def dfs(self, s, wordDict, stringList):
        if self.check(s, wordDict):
            
            if len(s) == 0:
                self.res.append(stringList[1:])
        
            for i in range(len(s)+1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, stringList +' '+ s[:i])
                    
            
        
    
    
    def check(self, s, wordDict):
        # dp[i] means in the position i-1 in the string, if I can get the answer that I want
        dp = [False for _ in range(len(s) + 1)]
        
        dp[0] = True
        
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        
        return dp[len(s)]
    
        
    
        
        
