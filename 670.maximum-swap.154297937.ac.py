#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (38.58%)
# Total Accepted:    21.3K
# Total Submissions: 55.3K
# Testcase Example:  '2736'
#
# 
# Given a non-negative integer, you could swap two digits at most once to get
# the maximum valued number. Return the maximum valued number you could get.
# 
# 
# Example 1:
# 
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# 
# 
# Example 2:
# 
# Input: 9973
# Output: 9973
# Explanation: No swap.
# 
# 
# 
# 
# Note:
# 
# The given number is in the range [0, 108]
# 
# 
#
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 往前走，记录maxIndex, 再往前走，走到一个位置发现当前的数比maxIndex要小，此时此刻可以记录 left 为 i right
        # 为maxIndex, 如过第一位是maxIndex的话 就根本不需要交换
        
        digits = list(str(num))

        left, right = 0, 0
        max_idx = len(digits) - 1
        
        for i in reversed(xrange(len(digits))):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[max_idx] > digits[i]:
                left, right = i, max_idx
        digits[left], digits[right] = digits[right], digits[left]
        return int("".join(digits))
    
