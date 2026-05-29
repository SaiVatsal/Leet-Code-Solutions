class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = 36
        for n in nums:
            res = min(res, n - 9 * ((n//10) + (n//100) + (n//1000) + (n//10000)))
            
        return res