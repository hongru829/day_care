#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (32.15%)
# Total Accepted:    200.7K
# Total Submissions: 624.3K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x.start)
        result_list = []
        compare_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start <= compare_interval.end:
                new_start = min(intervals[i].start,compare_interval.start)
                new_end = max(intervals[i].end, compare_interval.end)
                new_interval = Interval(new_start, new_end)
                compare_interval = new_interval
            else:
                result_list.append(compare_interval)
                compare_interval = intervals[i]
                
        result_list.append(compare_interval)
        return result_list
            
            
            
        
