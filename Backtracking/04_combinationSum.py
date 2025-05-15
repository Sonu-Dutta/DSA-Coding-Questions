from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            backtrack(i, cur, total+candidates[i])
            cur.pop()
            backtrack(i+1, cur, total)
        backtrack(0, [], 0)
        return res


obj = Solution()
print(obj.combinationSum([2, 3, 6, 7], 7))  # [[2,2,3],[7]]
print(obj.combinationSum([2, 3, 5], 8))  # [[2,2,2,2],[2,3,3],[3,5]]
