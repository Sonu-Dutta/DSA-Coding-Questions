from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

obj = Solution()
result = obj.validPath(n, edges, source, destination)
print(result)
