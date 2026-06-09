class Solution:
    def maxTotalValue(self, A: List[int], k: int) -> int:
        gMin = gMax = A[0]

        for n in A:
            gMin = min(gMin, n)
            gMax = max(gMax, n)

        return (gMax - gMin) * k