from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            currSum = max(nums[i], currSum + nums[i])
            if currSum > maxSum:
                maxSum = currSum

        return maxSum


if __name__ == "__main__":
    solution = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = solution.maxSubArray(nums)

    print("Input:", nums)
    print("Maximum Subarray Sum:", result)
