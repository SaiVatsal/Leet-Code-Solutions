class Solution:
    def minimumPushes(self, word: str) -> int:

        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1
        freq.sort()
        minPushing = 0
        pushCnt = 0

        for i in range(25, -1, -1):
            currEleIdx = 25 - i

            if currEleIdx % 8 == 0:
                pushCnt += 1
            minPushing += freq[i] * pushCnt

        return minPushing