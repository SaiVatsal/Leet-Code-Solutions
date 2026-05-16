class Solution:
    def findMin(self, nums: List[int]) -> int:
        while len(nums) > 1 and nums[-1] == nums[0]:
            nums.pop()

        return nums[bisect_left(nums, True, key=lambda n: n <= nums[-1])]