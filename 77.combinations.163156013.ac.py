#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (42.36%)
# Total Accepted:    151.9K
# Total Submissions: 358.7K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
# 
# Example:
# 
# 
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 
#
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        self.combinationHelper(n, k, temp, result, 1)
        print result
        return result
        
    def combinationHelper(self, n, k, temp, res, index):
        
        if len(temp) == k:
            res.append(temp)
            return
        
        for i in range(index, n + 1):
            self.combinationHelper(n, k, temp + [i], res, i + 1)
        
            
            
        
