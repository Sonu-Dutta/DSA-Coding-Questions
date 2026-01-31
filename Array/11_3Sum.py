def subarraySum(arr, target):
    left = 0
    sum = 0

    for i in range(len(arr)):
        sum += arr[i]

        while sum > target:
            sum -= arr[left]
            left += 1

        if sum == target:
            return (arr[left:i+1])


# Example usage:
print(subarraySum([1, 2, 3, 7, 5], 12))
# Output: [2, 3, 7]


# negative case
