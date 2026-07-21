class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')

        s = '1' + s + '1'

        n = len(s)
        i = 0

        ans = ones
        while i < n and s[i] == '1':
            i += 1
        c10 = 0
        while i < n and s[i] == '0':
            c10 += 1
            i += 1

        while i < n:
            c11 = 0
            while i < n and s[i] == '1':
                c11 += 1
                i += 1

            if c11 == 0:
                break
            c20 = 0
            while i < n and s[i] == '0':
                c20 += 1
                i += 1

            if c20 == 0:
                break

            ans = max(ans, ones + c10 + c20)
            c10 = c20

        return ans