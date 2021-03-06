#
# [833] Bus Routes
#
# https://leetcode.com/problems/bus-routes/description/
#
# algorithms
# Hard (32.80%)
# Total Accepted:    5.1K
# Total Submissions: 15.4K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# We have a list of bus routes. Each routes[i] is a bus route that the i-th bus
# repeats forever. For example if routes[0] = [1, 5, 7], this means that the
# first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->...
# forever.
# 
# We start at bus stop S (initially not on a bus), and we want to go to bus
# stop T. Travelling by buses only, what is the least number of buses we must
# take to reach our destination? Return -1 if it is not possible.
# 
# 
# Example:
# Input: 
# routes = [[1, 2, 7], [3, 6, 7]]
# S = 1
# T = 6
# Output: 2
# Explanation: 
# The best strategy is take the first bus to the bus stop 7, then take the
# second bus to the bus stop 6.
# 
# 
# Note: 
# 
# 
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 500.
# 0 <= routes[i][j] < 10 ^ 6.
# 
#
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        dic = {}
        queue = [S]
        if S == T:
            return 0
        
        for i in range(len(routes)):
            for stop in routes[i]:
                if stop not in dic:
                    dic[stop] = [i]
                else:
                    dic[stop].append(i)
        # print dic
        visited = set()
        countBuses = 0
        while queue:
            size = len(queue)
            countBuses += 1
            for k in range(size):
                stop = queue.pop(0)
                
                for bus in dic[stop]:
                    if bus in visited: 
                        continue
                    for busStop in routes[bus]:
                        if busStop == T:
                            return countBuses
                        queue.append(busStop)
                    visited.add(bus)

        return -1
                        
                    
        
