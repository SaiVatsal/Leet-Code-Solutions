class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i - 1] > nums[i] for i in range(len(nums))) < 2