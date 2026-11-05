class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        def far(a): 
            return all (abs(a - b) > d for b in arr2)

        return sum(map(far,arr1)) 