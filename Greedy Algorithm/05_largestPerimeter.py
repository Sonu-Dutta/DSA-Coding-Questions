from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i+2]+nums[i+1] > nums[i]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0


obj = Solution()
print(obj.largestPerimeter([2, 1, 2]))  # Output: 5
