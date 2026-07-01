from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0
        
        # 1. Multi-source BFS to calculate distance to the nearest thief for every cell
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        
        # 2. Use Dijkstra-like approach to find the path with the maximum "minimum" safeness factor
        # Max-heap to store (-safeness_factor, r, c)
        pq = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while pq:
            d, r, c = heapq.heappop(pq)
            d = -d # Convert back to positive
            
            if r == n - 1 and c == n - 1:
                return d
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # The safeness of the path is the minimum of current path safeness 
                    # and the distance of the new cell
                    new_safeness = min(d, dist[nr][nc])
                    heapq.heappush(pq, (-new_safeness, nr, nc))
                    
        return 0