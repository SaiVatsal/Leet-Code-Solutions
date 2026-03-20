class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = ""
        for i in range(len(nums)):
            if nums[i][i] == '0':
                result += '1'
            else:
                result += '0'
        return result