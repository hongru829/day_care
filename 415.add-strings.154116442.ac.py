#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (41.77%)
# Total Accepted:    57.4K
# Total Submissions: 137.3K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        result = 0
        res = ''
        carry = 0
        while i >=0 or j >=0:
            
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            
            if j >= 0:
                carry += int(num2[j])
                j -= 1
            
            res = str(carry % 10) + res
            carry = carry / 10
        
        return res if carry == 0 else '1' + res
            
            
        
