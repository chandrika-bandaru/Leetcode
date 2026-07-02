class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        min_health_lost = [[float('inf')] * n for _ in range(m)]
        
        start_cost = grid[0][0]
        if start_cost >= health:
            return False
        
        min_health_lost[0][0] = start_cost
        queue = deque([(0, 0)])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            r, c = queue.popleft()
            
            if r == m - 1 and c == n - 1:
                return health - min_health_lost[r][c] >= 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = min_health_lost[r][c] + grid[nr][nc]
                    
                    if new_cost < min_health_lost[nr][nc] and new_cost < health:
                        min_health_lost[nr][nc] = new_cost
                        
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))
                            
        return False      