class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        for i in range(len(piles) - 2, -1, -1):
            piles[i] += piles[i + 1]

        @cache
        def dfs(i, M):
            if i + M * 2 >= len(piles):
                return piles[i]

            return piles[i] - min(dfs(i + j, max(M, j)) for j in range(1, M * 2 + 1))

        return dfs(0, 1)
