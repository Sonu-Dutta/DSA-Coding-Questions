from typing import List


class Solution:
    def floodFill(self, img: List[List[int]], sr: int, sc: int, new_col: int) -> List[List[int]]:
        old_col = img[sr][sc]
        if old_col == new_col:
            return img

        rows, cols = len(img), len(img[0])

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and img[r][c] == old_col:
                img[r][c] = new_col
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        dfs(sr, sc)
        return img


obj = Solution()
img = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
new_col = 2
print(obj.floodFill(img, sr, sc, new_col))  # Output: [[2,2,2],[2,2,0],[2,0,1]]
