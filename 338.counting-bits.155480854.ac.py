#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (62.38%)
# Total Accepted:    113.5K
# Total Submissions: 181.9K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
# 
# 
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
# 
# 
# Follow up:
# 
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount  in c++ or in any other language.
# 
# 
# 
# Credits:Special thanks to @ syedee  for adding this problem and creating all
# test cases.
#
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        dp = [0]
        # 8的二进制是 1000 是由 100 转过来 这个时候 1的个数是不变的
        # 7的二进制是 0111 是由 3 011 转过来 这个时候 1的个数加一
        # 只要是奇数的话 奇数与1进行与操作都是为1
        # 相邻的2个数 进行与运算 能截取高位部分
        for i in xrange(1, num + 1):
            dp.append(dp[i >> 1] + (i & 1))
        return dp
        
