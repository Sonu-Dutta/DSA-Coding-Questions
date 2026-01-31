def zeroSumTriplets(num):
    num.sort()
    total = []

    for i in range(len(num)-2):
        if i > 0 and num[i] == num[i-1]:
            continue
        left = i+1
        right = len(num)-1

        while left < right:

            res = num[i]+num[left]+num[right]

            if res == 0:
                total.append([num[i], num[left], num[right]])

                while left < right and num[left] == num[left+1]:
                    left += 1

                while left < right and num[right] == num[right-1]:
                    right -= 1

                left += 1
                right -= 1

            elif res < 0:
                left += 1

            else:
                right -= 1

    return total


# Example usage:
print(zeroSumTriplets([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]
