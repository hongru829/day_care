#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (47.77%)
# Total Accepted:    238.4K
# Total Submissions: 499.2K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        ans = []
        self.backtracking(nums, temp, ans)
        return ans

    def backtracking(self, nums, temp, ans):
        if len(nums) == len(temp):
            ans.append(list(temp))
            return
        
        for i in range(len(nums)):
            if nums[i] in temp:
                continue
            temp.append(nums[i])
            self.backtracking(nums, temp, ans)
            temp.pop()
