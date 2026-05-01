class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        if not nums:
            return 0

        total_sum = sum(nums)
        n = len(nums)

        current_score = 0
        for i in range(n):
            current_score += i * nums[i]

        max_score = current_score

        for i in range(n - 1,0, -1):

            current_score = current_score + total_sum - (n * nums[i])
            max_score = max(max_score, current_score)
        
        return max_score


