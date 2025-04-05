def majorityElement(nums):
    count1 = 0
    count2 = 0

    candidate1 = 0
    candidate2 = 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    result = []
    threshold = len(nums) // 3

    if nums.count(candidate1) > threshold:
        result.append(candidate1)

    if candidate2 != candidate1 and nums.count(candidate2) > threshold:
        result.append(candidate2)

    return result


print(majorityElement([3, 2, 3]))


# if not nums:
#         return []
#     count1, count2, candidate1, candidate2 = 0, 0, 0, 1
#     for n in nums:
#         if n == candidate1:
#             count1 += 1
#         elif n == candidate2:
#             count2 += 1
#         elif count1 == 0:
#             candidate1, count1 = n, 1
#         elif count2 == 0:
#             candidate2, count2 = n, 1
#         else:
#             count1, count2 = count1 - 1, count2 - 1
#     return [n for n in (candidate1, candidate2)
#                     if nums.count(n) > len(nums) // 3]
