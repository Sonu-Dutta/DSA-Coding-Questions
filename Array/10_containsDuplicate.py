def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False


print(containsDuplicate([2, 3, 4, 5, 2, 1, 3]))
