class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        A = defaultdict(list)
        
        for u, v in edges:
            A[u].append(v)

            A[v].append(u)

        vis, res = [False] * n, 0
        for i, state in enumerate(vis):
            if not state:
                D = V = 0

                def dfs(x):
                    nonlocal V, D

                    V += 1
                    D += len(A[x])
                    vis[x] = True

                    for state in A[x]:
                        if not vis[state]:
                            dfs(state)


                dfs(i)
                res += D == V * (V - 1)

        return res