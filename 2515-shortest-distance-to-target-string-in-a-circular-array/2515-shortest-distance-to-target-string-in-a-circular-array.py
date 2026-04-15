class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float('inf')

        for i, word in enumerate(words):
            if word == target:
                dist = abs(i - startIndex)
                ans = min(ans, dist, n - dist)
        return - 1 if ans == float('inf') else ans 
        
        
