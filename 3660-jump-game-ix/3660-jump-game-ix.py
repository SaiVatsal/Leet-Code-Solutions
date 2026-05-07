class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n
        suf = [0] * n
        res = [0] * n

        # prefix max
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], nums[i])












        suf[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        res[-1] = pre[-1]

        # build answer
        for i in range(n - 2, -1, -1):

            # merge segment
            if pre[i] > suf[i + 1]:
                res[i] = res[i + 1]

            # new segment
            else:
                res[i] = pre[i]

        return res