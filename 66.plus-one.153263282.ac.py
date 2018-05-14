#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (39.84%)
# Total Accepted:    244.5K
# Total Submissions: 613.8K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
# 
#
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        arrSize = len(digits)
        last = digits[arrSize - 1] + 1
        
        if last < 10:
            digits[arrSize - 1] = last
            return digits
        
        else:
            for i in range(arrSize-1, -1, -1):
                if last > 9:
                    last = digits[i] + 1
                    digits[i] = last % 10
                else:
                    break
        
        if last > 9:
            return [1] + digits
        
        return digits
