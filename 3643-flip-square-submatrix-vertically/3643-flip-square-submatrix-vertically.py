class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
        # We iterate over the first half of the rows in the square submatrix
        for i in range(k // 2):
            top_row = x + i
            bottom_row = x + k - 1 - i
            # We swap the elements in the specified column range [y, y + k - 1] of the submatrix
            for j in range(y, y + k):
                grid[top_row][j], grid[bottom_row][j] = grid[bottom_row][j], grid[top_row][j]
        return grid