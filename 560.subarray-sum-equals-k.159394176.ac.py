#
# [560] Subarray Sum Equals K
#
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (39.93%)
# Total Accepted:    35.5K
# Total Submissions: 88.8K
# Testcase Example:  '[1,1,1]\n2'
#
# Given an array of integers and an integer k, you need to find the total
# number of continuous subarrays whose sum equals to k.
# 
# Example 1:
# 
# Input:nums = [1,1,1], k = 2
# Output: 2
# 
# 
# 
# Note:
# 
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the
# integer k is [-1e7, 1e7].
# 
# 
#
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
#         cumulative_sum  = [0 for _ in range(len(nums)+1)]
#         cumulative_sum[0] = 0
#         count = 0
#         for i in range(len(nums)):
#             cumulative_sum[i+1] = cumulative_sum[i] + nums[i]
        
#         for start in range(0, len(nums) + 1):
#             for end in range(start+1, len(nums) + 1):
#                 if cumulative_sum[end] - cumulative_sum[start] == k:
#                     count += 1
                
#         return count

        dic = {}
        dic[0] = 1
        cumulative_sum = 0
        count = 0
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            
            if cumulative_sum - k in dic:
                count += dic.get(cumulative_sum - k)
            
            if cumulative_sum not in dic:
                dic[cumulative_sum] = 1
            else:
                dic[cumulative_sum] += 1
        return count
            
