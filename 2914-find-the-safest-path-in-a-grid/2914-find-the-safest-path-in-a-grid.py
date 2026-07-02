class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        score = [[float('inf')] * n for _ in range(n)]

        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    score[i][j] = 0
                    q.append((i, j))
        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < n and 0 <= ny < n and
                        score[nx][ny] > score[x][y] + 1):
                    score[nx][ny] = score[x][y] + 1
                    q.append((nx, ny))

        visited = [[False] * n for _ in range(n)]
        pq = [(-score[0][0], 0, 0)]

        while pq:
            neg_safe, x, y = heapq.heappop(pq)
            safe = -neg_safe

            if x == n - 1 and y == n - 1:
                return safe

            if visited[x][y]:
                continue

            visited[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if (0 <= nx < n and 0 <= ny < n and
                        not visited[nx][ny]):

                    new_safe = min(safe, score[nx][ny])
                    heapq.heappush(pq, (-new_safe, nx, ny))

        return -1