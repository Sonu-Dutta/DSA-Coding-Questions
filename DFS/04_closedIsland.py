from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 1:
                return
            grid[i][j] = 1

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in [0, cols - 1]:
                if grid[i][j] == 0:
                    dfs(i, j)

        for j in range(cols):
            for i in [0, rows - 1]:
                if grid[i][j] == 0:
                    dfs(i, j)

        closedIslands = 0
        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    closedIslands += 1

        return closedIslands


grid = [
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0]
]

sol = Solution()
count = sol.closedIsland(grid)
print("Number of closed islands:", count)
print("Modified grid:")
for row in grid:
    print(row)
