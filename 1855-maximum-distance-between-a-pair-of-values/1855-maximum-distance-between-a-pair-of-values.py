class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = res = 0
        n, m = len(nums1), len(nums2)
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1   
        return res