from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1

        return result


# ---- Test code (this is what makes it run in VS Code) ----
if __name__ == "__main__":
    solution = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print("Output:", solution.intersect(nums1, nums2))  # [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print("Output:", solution.intersect(nums1, nums2))  # [4, 9]
