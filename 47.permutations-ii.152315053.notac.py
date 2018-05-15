#
# [47] Permutations II
#
# https://leetcode.com/problems/permutations-ii/description/
#
# algorithms
# Medium (35.37%)
# Total Accepted:    165.1K
# Total Submissions: 466.9K
# Testcase Example:  '[1,1,2]'
#
# Given a collection of numbers that might contain duplicates, return all
# possible unique permutations.
# 
# Example:
# 
# 
# Input: [1,1,2]
# Output:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
# 
#
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(temp) == len(nums):
            ans.append(list(temp))
        
        for i in range(len(nums)):
            if used[i] or i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            temp.append(nums[i])
            used[i] = True
            self.backtracking(nums, temp, ans, used)
            used[i] = False
            temp.pop()
