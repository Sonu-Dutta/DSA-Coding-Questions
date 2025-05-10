from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            grid[i][j] = -1

            while queue:
                x, y = queue.popleft()

                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = -1
                        queue.append((nx, ny))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    count += 1

        return count


grid = [
    [0, 1, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 0]
]

sol = Solution()
print(sol.numIslands(grid))
