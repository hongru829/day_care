#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (29.34%)
# Total Accepted:    36.1K
# Total Submissions: 122.9K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.  
# 
# You need to find the shortest such subarray and output its length.
# 
# Example 1:
# 
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
# 
# 
# 
# Note:
# 
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means . 
# 
# 
#
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        copy_num = nums[:]
        copy_num.sort()
        
        i, j = 0, len(nums) - 1
        
        while i < len(nums) and nums[i] == copy_num[i]:
            i += 1
        
        while j >= 0 and nums[j] == copy_num[j]:
            j -= 1
        
        min_len = max(0, j - i + 1)
        return min_len
