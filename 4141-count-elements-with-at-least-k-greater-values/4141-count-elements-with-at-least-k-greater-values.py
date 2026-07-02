class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k == 0: return len(nums)
        nums.sort()
        i = len(nums) - k
        n = nums[i]
        if n == nums[0]: return 0
        while n == nums[i]: i -= 1
        return i + 1