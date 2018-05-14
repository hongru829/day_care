#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (40.80%)
# Total Accepted:    127.8K
# Total Submissions: 313.2K
# Testcase Example:  '27'
#
# 
# ⁠   Given an integer, write a function to determine if it is a power of
# three.
# 
# 
# ⁠   Follow up:
# ⁠   Could you do it without using any loop / recursion?
# 
# 
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
#         if n <= 0:
#             return False
        
#         while n % 3 == 0:
#             n /= 3
        
#         return n == 1
        
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        if n % 3 == 0:
            return self.isPowerOfThree(n/3)
        
        else:
            return False
        
