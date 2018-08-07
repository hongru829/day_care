#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (49.74%)
# Total Accepted:    105.6K
# Total Submissions: 212.3K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
#
# Given a non-empty array of integers, return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
#
# Note:
#
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
#
#
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums_with_count = collections.defaultdict(int)
        for i in nums:
            nums_with_count[i] += 1
        sorted_nums = sorted(nums_with_count, key=nums_with_count.get, reverse=True)
        return sorted_nums[:k]
