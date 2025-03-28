def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


nums = [1, 1, 2, 2, 3]
print(removeDuplicates(nums))
