#
# [477] Total Hamming Distance
#
# https://leetcode.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (47.51%)
# Total Accepted:    32.5K
# Total Submissions: 68.5K
# Testcase Example:  '[4,14,2]'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Now your job is to find the total Hamming distance between all pairs of the
# given numbers.
# 
# 
# Example:
# 
# Input: 4, 14, 2
# 
# Output: 6
# 
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is
# 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6.
# 
# 
# 
# Note:
# 
# Elements of the given array are in the range of 0  to 10^9
# Length of the array will not exceed 10^4. 
# 
# 
#
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1   00000000000000001  
        # 2   00000000000..0100
        # 3   00000000000..0101
        # 4   00000000000..0100
        # 5   00000000000..0101
        # 6   00000000000..0110
        ans = 0
        for x in range(32):
            mask = 1 << x
            zero = one = 0
            
            for num in nums:
                if num & mask:
                    one += 1
                else:
                    zero += 1
            ans += zero * one
        return ans
        
