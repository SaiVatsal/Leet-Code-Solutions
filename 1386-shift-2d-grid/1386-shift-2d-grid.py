class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])
        total = m * n

        k %= total
        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):

                old_index = i * n + j

                new_index = (old_index + k) % total

                new_row = new_index // n
                new_col = new_index % n

                ans[new_row][new_col] = grid[i][j]

        return ans