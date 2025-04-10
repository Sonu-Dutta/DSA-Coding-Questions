from typing import List


class Solution:
    def numIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return
            if grid[i][j] == -1:
                return

            grid[i][j] = -1

            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
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
