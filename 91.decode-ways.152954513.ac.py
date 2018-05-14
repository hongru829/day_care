#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (20.41%)
# Total Accepted:    172.9K
# Total Submissions: 847.4K
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(2, len(s) + 1):
            if 10 <= int(s[i-2:i]) <= 26 and s[i-1] != '0':
                dp.append(dp[i-1] + dp[i-2])
            
            elif int(s[i-2: i]) == 10 or int(s[i-2: i]) == 20:
                dp.append(dp[i-2])
            
            elif s[i-1] != '0':
                dp.append(dp[i-1])
            
            else:
                return 0
        
        return dp[len(s)]
        
