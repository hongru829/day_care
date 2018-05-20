#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (51.12%)
# Total Accepted:    89.5K
# Total Submissions: 175.2K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [5,6]
# 
# 
#
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                if (nums[nums[i] - 1] > 0):
                    nums[nums[i] - 1] = -nums[nums[i] - 1]
                else:
                    continue
                    
            elif nums[i] < 0:
                if nums[abs(nums[i]) - 1] < 0:
                    continue
                else:
                    nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        
        return res
            
                
        
