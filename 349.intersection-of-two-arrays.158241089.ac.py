#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (48.48%)
# Total Accepted:    137.8K
# Total Submissions: 284.3K
# Testcase Example:  '[]\n[]'
#
# 
# Given two arrays, write a function to compute their intersection.
# 
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
# 
# 
# Note:
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
#
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1 = {}
        
        for i in range(len(nums1)):
            if nums1[i] in dic1:
                dic1[nums1[i]] += 1
            else:
                dic1[nums1[i]] = 1
        
        res = []
        for i in range(len(nums2)):
            if nums2[i] in dic1:
                res.append(nums2[i])
        
        return list(set(res))
                
                
                
            
        
