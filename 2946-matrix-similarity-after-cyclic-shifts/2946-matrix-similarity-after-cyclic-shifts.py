class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        # 1. Use len() instead of arrLen()
        # 2. Use 'mat' instead of 'matrix'
        m, n = len(mat), len(mat[0])
        
        # Optimize k: shifting n times is the same as 0 shifts
        k %= n
        if k == 0: return True
        
        for i in range(m):
            for j in range(n):
                # Check if the current element matches the one it 
                # would be compared to after k shifts.
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True