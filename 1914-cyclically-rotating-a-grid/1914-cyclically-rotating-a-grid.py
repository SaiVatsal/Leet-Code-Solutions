class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        layers = min(m, n) // 2

        for layer in range(layers):

            vals = []

            top = layer
            left = layer

            bottom = m - layer - 1
            right = n - layer - 1
            for j in range(left, right + 1):
                vals.append(grid[top][j])

            for i in range(top + 1, bottom):
                vals.append(grid[i][right])


            for j in range(right, left - 1, -1):
                vals.append(grid[bottom][j])


            for i in range(bottom - 1, top, -1):
                vals.append(grid[i][left])

            sz = len(vals)

            idx = k % sz

            for j in range(left, right + 1):

                grid[top][j] = vals[idx]

                idx += 1

                if idx == sz:
                    idx = 0
            for i in range(top + 1, bottom):

                grid[i][right] = vals[idx]

                idx += 1

                if idx == sz:
                    idx = 0
            for j in range(right, left - 1, -1):

                grid[bottom][j] = vals[idx]

                idx += 1

                if idx == sz:
                    idx = 0
            for i in range(bottom - 1, top, -1):

                grid[i][left] = vals[idx]

                idx += 1

                if idx == sz:
                    idx = 0

        return grid