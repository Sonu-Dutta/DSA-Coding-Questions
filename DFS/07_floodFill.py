def floodFill(matrix, r, c, x):
    rows = len(matrix)
    cols = len(matrix[0])
    i = matrix[r][c]

    if i == x:
        return matrix

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] != i:
            return
        matrix[r][c] = x

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    dfs(r, c)

    for row in matrix:
        print(row)

    return matrix


# Example usage:
# 10 by 10 matrix
matrix = [
    [3, 3, 3, 5, 3, 3, 3, 3, 3, 3],
    [3, 2, 2, 3, 5, 5, 3, 2, 2, 3],
    [3, 2, 2, 0, 5, 5, 3, 2, 2, 3],
    [3, 3, 0, 0, 3, 5, 3, 3, 3, 3],
    [5, 5, 3, 0, 2, 2, 3, 5, 5, 5],
    [5, 5, 3, 0, 0, 2, 3, 5, 5, 5],
    [5, 5, 3, 2, 2, 2, 3, 5, 5, 5],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [2, 2, 3, 5, 5, 3, 2, 2, 3, 3],
    [2, 2, 3, 5, 5, 3, 2, 2, 3, 3]
]
floodFill(matrix, 3, 2, 7)
