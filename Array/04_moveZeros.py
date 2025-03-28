def moveZeros(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


nums = [1, 0, 3, 0, 4]
print(moveZeros(nums))
