class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for digit in str(num):
                result.append(int(digit))

        return result
        