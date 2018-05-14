#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (33.91%)
# Total Accepted:    125.1K
# Total Submissions: 369K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input
# prerequisites.
# 
# 
# Hints:
# 
# 
# This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be
# impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera
# explaining the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.
# 
# 
#
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in xrange(numCourses)]
        visit = [0 for _ in xrange(numCourses)]
        
        for x, y in prerequisites:
            graph[x].append(y)
        
        def dfs(i):
            if visit[i] == -1:
                return False
            
            if visit[i] == 1:
                return True
            
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True
        
        for i in xrange(numCourses):
            if not dfs(i):
                return False
        return True
