from collections import deque
from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        visited = [[False] * cols for _ in range(rows)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right # down # left # up
        for i in range (rows):
            for j in range(cols):
                if not visited [i][j]:
                    q = deque([(i, j, -1, -1)])
                    visited[i][j] = True

                    while q:
                        r, c, pr, pc = q.popleft()
                        for dr, dc in directions:
                            nr,nc = r +dr,c +dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == grid[r]:
                                if not vistied [nr][nc]:
                                    visited[nr][nc] = True
                                    q.append((nr, nc, r, c))
                                elif (nr,nc) != (pr,pc):
                                    return True
        return False
        


