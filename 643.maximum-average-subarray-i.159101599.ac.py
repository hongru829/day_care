#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (37.80%)
# Total Accepted:    31.8K
# Total Submissions: 84.1K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
# 
# 
# Example 1:
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# Note:
# 
# 1 k n 
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# 
#
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        k_sum = 0
        count = k
        dic = {}
        for i in range(len(nums)):
            k_sum += nums[i]
            k -= 1
            if k == 0:
                dic[i] = k_sum / float(count)
                k_sum -= nums[i - count + 1]
                k += 1
        
        return max(dic.values())
        
            
                
                
        
