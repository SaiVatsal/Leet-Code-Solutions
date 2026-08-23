class Solution:
    def sumGame(self, A: str) -> bool:
        s, q = [0, 0], [0, 0]
        n = len(A)

        for i in range(n):
            j = i // (n // 2)
            if A[i] == '?':
                q[j] += 1
            else:
                s[j] += int(A[i])

        return (q[0] + q[1]) & 1 == 1 or (s[0] - s[1]) != (q[1] - q[0]) * 4.5