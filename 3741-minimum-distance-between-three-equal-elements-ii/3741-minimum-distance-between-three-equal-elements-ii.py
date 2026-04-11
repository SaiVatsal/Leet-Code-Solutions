from collections import defaultdict
from typing import List
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        indices = defaultdict(list)
        min_dist = float('inf')

        for i, num in enumerate(nums):
            indices[num].append(i)

        for idx_list in indices.values():
            if len(idx_list) >= 3:
                for j in range(len(idx_list) - 2):
                    i, k = idx_list[j], idx_list[j+2]
                    dist = 2 * (k - i)
                    min_dist = min(min_dist, dist)

        return -1 if min_dist == float('inf') else min_dist
        
        
        