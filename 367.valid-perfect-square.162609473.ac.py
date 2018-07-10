#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (38.80%)
# Total Accepted:    77.6K
# Total Submissions: 200K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# 
# Input: 16
# Returns: True
# 
# 
# 
# Example 2:
# 
# Input: 14
# Returns: False
# 
# 
# 
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        
        if num < 4 and num > 1:
            return False
        
        if num == 4:
            return True
        
        left = 0
        right = num / 2
        while left + 1 < right:
            mid = (left + right) / 2
            
            sqrtNum = mid * mid
            
            if sqrtNum == num:
                return True
            
            elif sqrtNum > num:
                right = mid - 1
            
            elif sqrtNum < num:
                left = mid + 1
        
        if left * left == num:
            return True
        if right * right == num:
            return True
        
        return False
                
            
            
            
            
            
            
            
        
