#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (40.82%)
# Total Accepted:    172.9K
# Total Submissions: 423.5K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        if n % 2 == 0:
            return self.isPowerOfTwo(n / 2)
        
        else:
            return False
