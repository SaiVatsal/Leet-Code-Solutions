class Solution:
    def earliestFinishTime(
        self, la: list[int], lb: list[int], wa: list[int], wb: list[int]
    ) -> int:
        MAX = 300005
        l = w = minL = minW = MAX
        n, m = len(la), len(wa)

        for i in range(n):
            l = min(l, la[i] + lb[i])

        for i in range(m):
            w = min(w, wa[i] + wb[i])
            minL = min(minL, max(wa[i], l) + wb[i])

        for i in range(n):
            minW = min(minW, max(la[i], w) + lb[i])

        return min(minW, minL)