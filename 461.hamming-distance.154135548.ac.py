#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (69.51%)
# Total Accepted:    155.1K
# Total Submissions: 223.2K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 231.
# 
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
#
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            if x & 1 != y & 1:
                count += 1
            x = x >> 1
            y = y >> 1
        
        return count
        
