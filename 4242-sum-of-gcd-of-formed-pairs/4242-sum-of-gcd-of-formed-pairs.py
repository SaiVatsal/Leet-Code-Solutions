class Solution:
    def gcdSum(self, A: list[int]) -> int:
        maxi, n = 0, len(A)

        for i in range(n):
            maxi = max(maxi, A[i])
            A[i] = gcd(A[i], maxi)

        A.sort()

        return sum(gcd(A[i], A[~i]) for i in range(n // 2))