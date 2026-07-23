class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)        
        return 1 << (n.bit_length() - 3 // (n + 1))