#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (34.31%)
# Total Accepted:    202.5K
# Total Submissions: 590.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res = str(carry%2) + res
            carry /= 2
        return res if not carry else "1" + res
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """ 
#         alen = len(a) - 1
#         blen = len(b) - 1
#         flag = 0
#         res = ''
        
#         while alen >= 0 and blen >= 0:
#             summer = int(a[alen]) + int(b[blen]) + flag
#             digit = summer % 2
#             flag = summer / 2
#             alen -= 1
#             blen -= 1
#             res = str(digit) + res
            
#         while alen >= 0:
#             summer = int(a[alen]) + flag
#             digit = summer % 2
#             flag = summer / 2
#             alen -= 1
#             res = str(digit) + res
            
#         while blen >= 0:
#             summer = int(b[blen]) + flag
#             digit = summer % 2
#             flag = summer / 2
#             blen -= 1
#             res = str(digit) + res
        
#         if flag > 0:
#             res = str(flag) + res
        
#         return res

        
        
    
                
                
            

                
