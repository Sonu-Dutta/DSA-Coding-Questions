from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(temp: List[int]):
            if len(nums) == len(temp):
                res.append(temp[:])
                return

            for n in nums:
                if n in temp:
                    continue
                temp.append(n)
                backtrack(temp)
                temp.pop()

        backtrack([])
        return res


obj = Solution()
nums = [1, 2, 3]
result = obj.permute(nums)
print(result)
