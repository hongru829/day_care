#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (44.22%)
# Total Accepted:    109.5K
# Total Submissions: 247.5K
# Testcase Example:  '[]\n[]'
#
# 
# Given two arrays, write a function to compute their intersection.
# 
# 
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
# 
# 
# Note:
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# 
# Follow up:
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums1)):
            if nums1[i] in dic:
                dic[nums1[i]] += 1
            else:
                dic[nums1[i]] = 1
        res = []
        for i in range(len(nums2)):
            if nums2[i] in dic and dic[nums2[i]] > 0:
                res.append(nums2[i])
                dic[nums2[i]] -= 1
        
        return res
