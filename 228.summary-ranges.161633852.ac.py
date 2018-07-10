#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (32.89%)
# Total Accepted:    104.1K
# Total Submissions: 316.6K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# 
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# 
# 
# Example 2:
# 
# 
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# 
# 
#
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        
        if not nums:
            return []
        
        res = []
        start = 0
        i = 0
        
        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i+1]:
                res.append(self.helper(nums[start], nums[i]))
                start = i + 1
            i += 1
        res.append(self.helper(nums[start], nums[i]))
        return res
    
    def helper(self, l, r):
        
        return str(l) if l == r else str(l) + "->" + str(r)
        
