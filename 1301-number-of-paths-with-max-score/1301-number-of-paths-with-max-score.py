class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp_sum = [[-1] * n for _ in range(n)]
        dp_count = [[0] * n for _ in range(n)]
        
        dp_sum[n-1][n-1] = 0
        dp_count[n-1][n-1] = 1
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or dp_sum[i][j] == -1:
                    continue
                
                for di, dj in [(0, -1), (-1, 0), (-1, -1)]:
                    ni, nj = i + di, j + dj
                    
                    if ni >= 0 and nj >= 0 and board[ni][nj] != 'X':
                        cell_val = 0
                        if '0' <= board[ni][nj] <= '9':
                            cell_val = int(board[ni][nj])
                        
                        new_sum = dp_sum[i][j] + cell_val
                        
                        if new_sum > dp_sum[ni][nj]:
                            dp_sum[ni][nj] = new_sum
                            dp_count[ni][nj] = dp_count[i][j]
                        elif new_sum == dp_sum[ni][nj]:
                            dp_count[ni][nj] = (dp_count[ni][nj] + dp_count[i][j]) % MOD
                            
        res_sum = max(0, dp_sum[0][0])
        res_count = dp_count[0][0] if dp_sum[0][0] != -1 else 0
        
        return [res_sum, res_count]