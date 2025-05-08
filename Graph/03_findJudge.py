class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1 and not trust:
            return 1

        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)

        for a, b in trust:
            indegree[b] += 1
            outdegree[a] += 1

        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i

        return -1


object = Solution()
n = 4
trust = [[1, 2], [3, 2], [4, 2]]
print(object.findJudge(n, trust))  # Output: -1
