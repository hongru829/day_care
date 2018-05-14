#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.39%)
# Total Accepted:    409.4K
# Total Submissions: 1.7M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        answer = 0
        sign = 1 if x > 0 else -1
        x = abs(x)
        
        while x > 0:
            answer = answer * 10 + x % 10
            x = x / 10
        
        if sign * answer < 2**31-1 and sign * answer > -2**31:
            return sign * answer
        else:
            return 0
        
