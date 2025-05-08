from typing import List


class Solution:
    def dfs(self, adj: List[List[int]], curr: int, color: List[int], currColor: int) -> bool:
        color[curr] = currColor

        for neighbor in adj[curr]:
            if color[neighbor] == color[curr]:
                return False
            if color[neighbor] == -1:
                if not self.dfs(adj, neighbor, color, 1 - currColor):
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        V = len(graph)
        color = [-1] * V

        for i in range(V):
            if color[i] == -1:
                if not self.dfs(graph, i, color, 1):
                    return False
        return True


obj = Solution()
graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(obj.isBipartite(graph))  # Output: True
