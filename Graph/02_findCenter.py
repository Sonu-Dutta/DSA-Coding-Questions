from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Take the first two edges
        edge1 = edges[0]
        edge2 = edges[1]

        print(f"First edge: {edge1}")
        print(f"Second edge: {edge2}")

        # Compare nodes to find the one common in both
        if edge1[0] == edge2[0] or edge1[0] == edge2[1]:
            print(f"Center found: {edge1[0]}")
            return edge1[0]
        else:
            print(f"Center found: {edge1[1]}")
            return edge1[1]


# Test the debug version
edges = [[1, 2], [2, 3], [4, 2]]
solution = Solution()
print("Final Result:", solution.findCenter(edges))
