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
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in xrange(1, N+1)}
        seen = [False] * (N+1)
        dist[K] = 0

        while True:
            cand_node = -1
            cand_dist = float('inf')
            for i in xrange(1, N+1):
                if not seen[i] and dist[i] < cand_dist:
                    cand_dist = dist[i]
                    cand_node = i

            if cand_node < 0: break
            seen[cand_node] = True
            for nei, d in graph[cand_node]:
                dist[nei] = min(dist[nei], dist[cand_node] + d)

        ans = max(dist.values())
        return ans if ans < float('inf') else -1
    
# class Solution(object):
#     def networkDelayTime(self, times, N, K):
#         graph = collections.defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((v, w))

#         pq = [(0, K)]
#         dist = {}
#         while pq:
#             d, node = heapq.heappop(pq)
#             if node in dist: continue
#             dist[node] = d
#             for nei, d2 in graph[node]:
#                 if nei not in dist:
#                     heapq.heappush(pq, (d+d2, nei))

#         return max(dist.values()) if len(dist) == N else -1
                
        
        
