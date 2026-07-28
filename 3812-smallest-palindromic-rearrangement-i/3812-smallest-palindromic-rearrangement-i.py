class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = [0] * 26

        for c in s:

            cnt[ord(c) - ord('a')] += 1

        left = []
        mid = ""

        for i in range(26):
            
            left.extend(chr(ord('a') + i) * (cnt[i] // 2))
            if cnt[i] % 2:
                mid = chr(ord('a') + i)

        left = "".join(left)
        return left + mid + left[::-1]