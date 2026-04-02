from functools import cache
import math

class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])

        @cache
        def dfs(r, c, k):
            if r >= m or c >= n:
                return -math.inf
            
            current_val = coins[r][c]
            
            if r == m - 1 and c == n - 1:
                res = current_val
                if k > 0 and current_val < 0:
                    res = max(res, 0)
                return res

            res = current_val + max(dfs(r + 1, c, k), dfs(r, c + 1, k))

            if k > 0 and current_val < 0:
                res = max(res, max(dfs(r + 1, c, k - 1), dfs(r, c + 1, k - 1)))
            
            return res

        return dfs(0, 0, 2)