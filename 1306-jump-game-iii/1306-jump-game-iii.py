from collections import deque

class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        q = deque([start])
        visited = set([start])
        
        while q:
            curr = q.popleft()
            
            if arr[curr] == 0:
                return True
                
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < len(arr) and next_idx not in visited:
                    visited.add(next_idx)
                    q.append(next_idx)
                    
        return False