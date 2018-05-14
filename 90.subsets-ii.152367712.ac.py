#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (38.55%)
# Total Accepted:    147.6K
# Total Submissions: 382.7K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        res =[]
        nums.sort()
        self.backtracking(nums, temp, res, 0)
        return res
    
    def backtracking(self, nums, temp, res, start):
        res.append(list(temp))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.backtracking(nums, temp, res, i+1)
            temp.pop()
        
