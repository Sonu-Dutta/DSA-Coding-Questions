from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}

        for i, num in enumerate(nums):
            if num in last_index:
                if i - last_index[num] <= k:
                    return True

            last_index[num] = i

        return False


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 0, 1, 1]
    k = 1

    result = solution.containsNearbyDuplicate(nums, k)

    print("Input nums:", nums)
    print("k:", k)
    print("Contains nearby duplicate:", result)
