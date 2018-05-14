#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (24.75%)
# Total Accepted:    488.1K
# Total Submissions: 2M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# 
# Given "bbbbb", the answer is "b", with the length of 1.
# 
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the
# answer must be a substring, "pwke" is a subsequence and not a substring.
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        res = 0
        start = 0
        for i in range(len(s)):
            if s[i] in dic and start <= dic[s[i]]:
                start = dic[s[i]] + 1
            else:
                res = max(res, i - start + 1)
            dic[s[i]] = i
        return res
#     # 如果是longest with repeating character
    
#     def lengthOfLongestSubstring(self, s):
#         dic = {}
#         start = 0
#         res = 0
#         for i in range(len(s)):
#             if len(dic) == 0:
#                 dic[s[i]] = i 
#             if s[i] in dic and len(dic) == 1:
#                 res = max(res, i - start + 1)
#             else:
#                 start = i
#                 dic.clear()
#         return res
