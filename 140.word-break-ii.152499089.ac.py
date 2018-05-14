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
        
    
    def check(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        
        for i in range(1, len(s)+1):
            for k in range(0, i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[len(s)]
    
    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            if len(s) == 0:
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])
    
    def wordBreak(self, s, wordDict):
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res
