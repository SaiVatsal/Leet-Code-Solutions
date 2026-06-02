class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        n = len(landStartTime)
        m = len(waterStartTime)

        for i in range(n):
            for j in range(m):
                land_finish = landStartTime[i] + landDuration[i]
                finish1 = max(land_finish, waterStartTime[j]) + waterDuration[j]
                water_finish = waterStartTime[j] + waterDuration[j]
                finish2 = max(water_finish, landStartTime[i]) + landDuration[i]

                ans = min(ans, finish1, finish2)

        return ans