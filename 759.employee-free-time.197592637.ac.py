# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, schedules):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        m_intervals = []
        for schedule in schedules:
            for sch in schedule:
                m_intervals.append(sch)
        
        m_intervals = sorted(m_intervals, key=lambda x: x.start)
        comparted_interval = m_intervals[0]
        
        res = []
        for i in range(1, len(m_intervals)):
            if m_intervals[i].start > comparted_interval.end:
                res.append(comparted_interval)
                comparted_interval = m_intervals[i]
            else:
                minStart = min(comparted_interval.start, m_intervals[i].start)
                maxEnd = max(comparted_interval.end, m_intervals[i].end)
                newInterval = Interval(minStart, maxEnd)
                comparted_interval = newInterval
        res.append(comparted_interval)
        
        results = []
        for i in range(len(res) - 1):
            first_interval = res[i]
            second_interval= res[i+1]
            if second_interval.start - first_interval.end > 0:
                results.append(Interval(first_interval.end, second_interval.start))
        return results
                
            
        
        
        
        
        
        
        
        
        
        
        
        
                

            
