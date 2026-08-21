from typing import List
from math import gcd
## moduels
class Solution:

    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
# arranges
        useful = []

        for coin in coins:
            redundant = False

            for prev in useful:
                if coin % prev == 0:
                    redundant = True
                    break

            if not redundant:
                useful.append(coin)

        low = 1
        high = useful[0] * k

        m = len(useful)
        total_masks = 1 << m

        lcms = [1] * total_masks

        signs = [1] * total_masks

        for mask in range(1, total_masks):
            current_lcm = 1
            bits = 0

            for i in range(m):
                if mask & (1 << i):
                    current_lcm //= gcd(current_lcm, useful[i])

                    if current_lcm > high // useful[i]:
                        current_lcm = high + 1
                        break

                    current_lcm *= useful[i]
                    bits += 1

            lcms[mask] = current_lcm

            signs[mask] = 1 if bits % 2 == 1 else -1

        def count(x: int) -> int:
            result = 0

            for mask in range(1, total_masks):
                if lcms[mask] <= x:
                    result += signs[mask] * (x // lcms[mask])

            return result

        while low < high:
            mid = low + (high - low) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low