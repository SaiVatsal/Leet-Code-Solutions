class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [num for row in grid for num in row]
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        nums.sort()
        target = nums[len(nums) // 2]
        return sum(abs(num - target) // x for num in nums)