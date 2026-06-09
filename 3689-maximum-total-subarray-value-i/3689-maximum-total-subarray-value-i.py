class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mx = 0
        mn = float('inf')

        for num in nums:
            if num > mx:
                mx = num

            if num < mn:
                mn = num

        return (mx - mn) * k