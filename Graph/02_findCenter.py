from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge1 = edges[0]
        edge2 = edges[1]

        if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
            return edge1[0]
        return edge1[1]


edges = [[1, 2], [2, 3], [4, 2]]
solution = Solution()
print(solution.findCenter(edges))
