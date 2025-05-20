from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i = j = 0
        while len(g) > i and len(s) > j:
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


obj = Solution()
g = [1, 2, 3]
s = [1, 1]
print(obj.findContentChildren(g, s))  # Output: 1
