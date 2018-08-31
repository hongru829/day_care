#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (33.82%)
# Total Accepted:    105.8K
# Total Submissions: 312.9K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# 
#
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # i means the length of array
        # for example:
        # dp[0] = 0
        # dp[1] = nums[0]
        # dp[2] = nums[0] + nums[1]
        # dp[3] = nums[0] + nums[1] + nums[2]
        # dp[4] = nums[0] + nums[1] + nums[2] + nums[3]
        # dp[5] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4]
        # dp[6] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5]
        # if want to get sumRange(2, 5) it means we need to get nums[2] + nums[3] + nums[4] + nums[5]
        # sumRange(2, 5) actually measn sumRange(2, 5) = dp[6] - dp[2]
        # sumRange(i, j) actuallt means sumRange(i, j) = dp[j+1] - dp[i]
        self.dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.dp[i] = self.dp[i-1] + nums[i-1]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
