def removeElement(arr, val):
    k = 0
    for i in arr:
        if i != val:
            arr[k] = i
            k += 1
    return k


print(removeElement([10, 21, 2, 2, 19, 0, 4, 2], 2))
