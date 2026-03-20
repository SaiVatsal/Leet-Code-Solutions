class Solution:
    def minAbsDiff(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                unique_vals = set()
                
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        unique_vals.add(grid[r][c])
                
                if len(unique_vals) < 2:
                    ans[i][j] = 0
                else:
                    sorted_vals = sorted(list(unique_vals))
                    min_diff = float('inf')
                    
                    for idx in range(1, len(sorted_vals)):
                        diff = sorted_vals[idx] - sorted_vals[idx - 1]
                        if diff < min_diff:
                            min_diff = diff
                            
                    ans[i][j] = min_diff
                    
        return ans