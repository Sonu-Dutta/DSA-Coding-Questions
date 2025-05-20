# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    # This is a placeholder for the actual guess function.
    # In a real scenario, this function would compare the guessed number with a secret number.
    # For example, let's assume the picked number is 6.
    picked_number = 6
    if num < picked_number:
        return 1
    elif num > picked_number:
        return -1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1

# Example usage:


obj = Solution()
n = 10
print(obj.guessNumber(n))  # Output: 6 (assuming the picked number is 6)
