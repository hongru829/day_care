#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (30.04%)
# Total Accepted:    53.2K
# Total Submissions: 177.2K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
# 
# Note:
# 
# 
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# 
# 
# Example 1:
# 
# 
# Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR",
# "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# Example 2:
# 
# 
# Input: tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
# 
# 
#
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = {}
        
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]] = [ticket[1]]
            else:
                graph[ticket[0]].append(ticket[1])
        
    
    
        def dfs(stop, graph, res, tickets):
            if len(res) == len(tickets) + 1:
                return True
            
            if stop not in graph:
                return False
            
                
            for neighbor in sorted(graph[stop]):
                res.append(neighbor)
                graph[stop].remove(neighbor)
                if dfs(neighbor, graph, res, tickets):
                    return True
                res.pop()
                graph[stop].append(neighbor)
            
            return False
        
        res = ['JFK']
        dfs('JFK', graph, res, tickets)
        return res
            
        
        
