#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (28.99%)
# Total Accepted:    232.8K
# Total Submissions: 803K
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        
        if x == 4:
            return 2
        
        maxRange = x // 2
        left, right = 1, maxRange
        
        while left + 1 < right:
            mid = (left + right)/ 2
            curr_sq = mid * mid
            next_sq = (mid + 1) * (mid + 1)
            
            if curr_sq <= x and next_sq > x:
                return mid
            
            if curr_sq < x:
                left = mid
            
            if curr_sq > x:
                right = mid
        
        if right*right <= x: 
            return right
        if left*left <= x: 
            return left
        
