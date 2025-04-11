from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or grid2[i][j] == 0:
                return True

            grid2[i][j] = 0

            sub = grid1[i][j] == 1

            sub = dfs(i, j+1) and sub
            sub = dfs(i+1, j) and sub
            sub = dfs(i-1, j) and sub
            sub = dfs(i, j-1) and sub
            return sub

        count = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        return count


grid1 = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1]
]

grid2 = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1]
]

sol = Solution()
count = sol.countSubIslands(grid1, grid2)
print(count)
