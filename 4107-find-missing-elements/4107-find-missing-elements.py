class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        result = []
        for val in range(min_val, max_val + 1):
            if val not in num_set:
                result.append(val)
                
        return result