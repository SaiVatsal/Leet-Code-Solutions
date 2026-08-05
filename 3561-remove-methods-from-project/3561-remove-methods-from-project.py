class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        edges = [[] for _ in range(n)]
        in_degree = [0] * n

        for u, v in invocations:
            edges[u].append(v)
            in_degree[v] += 1

        queue = collections.deque([k])
        sus = bytearray(n)
        sus[k] = 1

        while queue:
            u = queue.popleft()
            for v in edges[u]:
                in_degree[v] -= 1

                if sus[v] == 0:
                    queue.append(v)
                    sus[v] = 1

        can_remove_all = True
        for i in range(n):
            if sus[i] == 1 and in_degree[i] > 0:
                can_remove_all = False
                break

        if not can_remove_all:
            return list(range(n))

        return [i for i in range(n) if sus[i] == 0]
