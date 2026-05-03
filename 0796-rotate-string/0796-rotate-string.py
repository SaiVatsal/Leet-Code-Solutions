class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):

            return False

        doubled = s + s

        return goal in doubled