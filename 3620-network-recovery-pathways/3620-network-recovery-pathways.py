import heapq
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        max_c = 0
        for u, v, c in edges:
            if online[u] and online[v]:
                adj[u].append((v, c))
                max_c = max(max_c, c)
        
        def can_reach_with_min_cost(min_threshold):
            # Dijkstra to find the shortest path using edges >= min_threshold
            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]  # (cost, node)
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > dist[u]:
                    continue
                if u == n - 1:
                    return d <= k
                
                for v, cost in adj[u]:
                    if cost >= min_threshold:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            heapq.heappush(pq, (dist[v], v))
            return dist[n - 1] <= k

        # Binary Search
        low = 0
        high = max_c
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_reach_with_min_cost(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans