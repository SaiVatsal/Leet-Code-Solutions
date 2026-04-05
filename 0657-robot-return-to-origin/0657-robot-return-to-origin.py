class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Check if Up cancels Down, and Right cancels Left
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')