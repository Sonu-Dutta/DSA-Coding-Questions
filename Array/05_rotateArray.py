def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]

rotate(nums, 3)
print(nums)
