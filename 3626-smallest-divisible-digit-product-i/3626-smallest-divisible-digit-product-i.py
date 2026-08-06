class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        q, r = divmod(n, 10)
        
        req = t // gcd(max(q, 1), t)
        nxt = ((r + req - 1) // req) * req
        x = nxt - (nxt - 10) * (nxt // 10)
        return q * 10 + x