#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (15.73%)
# Total Accepted:    133.8K
# Total Submissions: 850.4K
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero.
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# 
# Note:
# 
# 
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 231 − 1 when the division
# result overflows.
# 
# 
#
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            if abs(dividend) < abs(divisor):
                return 0
        summer = 0; count = 0; res = 0
        a = abs(dividend); b = abs(divisor)
        while a >= b:
            summer = b
            count = 1
            while summer + summer <= a:
                summer += summer
                count += count
            a -= summer
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        return res
    
    
