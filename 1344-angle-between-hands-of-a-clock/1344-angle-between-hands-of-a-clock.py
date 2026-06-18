class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        x = hour + minutes / 60
        diff = (11 * x) % 12
        return min(diff, 12 - diff) * 30
        