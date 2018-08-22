#
# [744] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Medium (36.64%)
# Total Accepted:    10.8K
# Total Submissions: 29.6K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# 
# There are N network nodes, labelled 1 to N.
# 
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
# 
# Now, we send a signal from a certain node K.  How long will it take for all
# nodes to receive the signal?  If it is impossible, return -1.
# 
# 
# Note:
# 
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1  and 1 .
# 
# 
#
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        
        dist = {node: float('inf') for node in range(1, N + 1)}
        
        def dfs(node, elapsed):
            if elapsed >=  dist[node]:
                return
            dist[node] = elapsed
            for time, nei in sorted(graph[node]):
                dfs(nei, elapsed + time)
        
        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1
        
