class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using for loop
        for i in range(len(nums)):
            # length of the number
            #i + 1
            for j in range(i + 1, len(nums)):
                # using if else statement
                
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]
        return []
