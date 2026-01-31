from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def swap(i: int, j: int):
            nums[i], nums[j] = nums[j], nums[i]

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                swap(low, mid)
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                swap(mid, high)
                high -= 1


obj = Solution()
nums = [2, 0, 2, 1, 1, 0]
obj.sortColors(nums)
print(nums)  # Output should be [0, 0, 1, 1, 2, 2]
