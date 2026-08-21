class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        coins.sort()
         
        A = []
        for c in coins:

            if all(c % x for x in A):
                A.append(c)

        n = len(A)

        def check(mid):
            tot = 0
            for i in range(1, n + 1):
                q = (1 << i) - 1
                lim = 1 << n
                sgn = ((i & 1) << 1) - 1

                while q < lim:
                    x = 1
                    for j in range(n):
                        if (q >> j) & 1:
                            x = lcm(x, A[j])

                    tot += (mid // x) * sgn

                    c = q & -q
                    r = q + c
                    q = (((r ^ q) >> 2) // c) | r
            return tot >= k
 
        return bisect_left(range(A[0] * k + 1), True, lo=k, key=check)
