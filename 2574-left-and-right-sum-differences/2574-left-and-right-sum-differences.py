class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)

        left_sum = 0
        result = []

        for num in nums:
            right_sum -= num
            result.append(abs(left_sum - right_sum))
            left_sum += num

        return result