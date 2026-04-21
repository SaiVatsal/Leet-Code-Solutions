from collections import defaultdict
from typing import List
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i]) 
            return parent[i]
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
        for u, v in allowedSwaps:
            union(u, v)

        components = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            root = find(i)
            components[root][source[i]] += 1
            

        matches = 0
        for i in range(n):
            root = find(i)
            val = target[i]
            

            if components[root][val] > 0:
                components[root][val] -= 1
                matches += 1
                
      
        return n - matches