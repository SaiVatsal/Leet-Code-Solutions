class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:

            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':

            return False
        
        visited = set()
        
        def dfs(r, c, bal):
            if bal < 0 or bal > (m + n) // 2:
                return False
            
            if r == m - 1 and c == n - 1:

                return bal == 0
            
            state = (r, c, bal)
            if state in visited:
                return False
            visited.add(state)
            
            if r + 1 < m:
                nxt = bal + (1 if grid[r + 1][c] == '(' else -1)
                if dfs(r + 1, c, nxt):
                    return True
                    
            if c + 1 < n:
                nxt = bal + (1 if grid[r][c + 1] == '(' else -1)
                
                if dfs(r, c + 1, nxt):
                    return True
                    
            return False
        
        return dfs(0, 0, 1)