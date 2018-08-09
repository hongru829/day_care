#
# [820] Find Eventual Safe States
#
# https://leetcode.com/problems/find-eventual-safe-states/description/
#
# algorithms
# Medium (39.16%)
# Total Accepted:    6.9K
# Total Submissions: 17.7K
# Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
#
# In a directed graph, we start at some node and every turn, walk along a
# directed edge of the graph.  If we reach a node that is terminal (that is, it
# has no outgoing directed edges), we stop.
# 
# Now, say our starting node is eventually safe if and only if we must
# eventually walk to a terminal node.  More specifically, there exists a
# natural number K so that for any choice of where to walk, we must have
# stopped at a terminal node in less than K steps.
# 
# Which nodes are eventually safe?  Return them as an array in sorted order.
# 
# The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the
# length of graph.  The graph is given in the following form: graph[i] is a
# list of labels j such that (i, j) is a directed edge of the graph.
# 
# 
# Example:
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Here is a diagram of the above graph.
# 
# 
# 
# 
# 
# Note:
# 
# 
# graph will have length at most 10000.
# The number of edges in the graph will not exceed 32000.
# Each graph[i] will be a sorted list of different integers, chosen within the
# range [0, graph.length - 1].
# 
#
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # color[i] == 1 means is visiting
        # color[i] == 2 means has been visited and exit the dfs
        # color[i] == 0 means has not been visited
        def dfs(i, graph, color):
            
            if color[i] > 0:
                return color[i] == 2
            
            color[i] = 1
            for nei in graph[i]:
                if color[nei] == 2:
                    continue
                if color[nei] == 1 or dfs(nei, graph, color) == False:
                    return False
            color[i] = 2
            return True
            
        
        res = []
        color = [0]* len(graph)
        for i in range(len(graph)):
            if dfs(i, graph, color):
                res.append(i)
        
        return res
                        
                        
                
                
                
            