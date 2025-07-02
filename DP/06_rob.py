from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        p1 = nums[0]
        p2 = max(nums[0], nums[1])

        for i in range(2, n):
            cur = max(p1+nums[i], p2)
            p1 = p2
            p2 = cur

        return p2


obj = Solution()
print(obj.rob([2, 7, 9, 3, 1]))  # Output: 12
