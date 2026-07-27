class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return ((x:=sorted(nums)[-2:])[-1]-1)*(x[-2]-1) 