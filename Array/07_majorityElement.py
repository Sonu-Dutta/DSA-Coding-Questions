def majorityElement(nums):
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


print(majorityElement([1, 2, 3, 1, 2, 3, 4, 2, 1, 1]))
