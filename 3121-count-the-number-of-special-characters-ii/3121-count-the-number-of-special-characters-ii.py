class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        A = [[False, False] for _ in range(27)]

        for ch in word:
            i = ord(ch) & 31
            c = ord(ch) >> 5 & 1
            A[i][c] = not (c and A[i][0])

        return sum(u and v for u, v in A)