def nextGreaterElement(arr):
    stack = []
    res = [-1] * len(arr)
    print(res)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])

    return res


arr = [4, 5, 2, 10, 8]
print(nextGreaterElement(arr))  # Output: [5, 10, 10, -1, -1]
