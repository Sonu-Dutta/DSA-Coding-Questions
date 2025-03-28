def twoSum(nums, target):
    numDict = {}
    for i, num in enumerate(nums):
        remains = target-num
        if remains in numDict:
            return (numDict[remains], i)
        numDict[num] = i
    return []


print(twoSum([21, 3, 17, 12, 2], 19))
