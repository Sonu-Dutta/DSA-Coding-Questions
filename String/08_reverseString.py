# Reverse String – (LeetCode 344)

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        print("s-> ", s)


obj = Solution()
result = obj.reverseString(["h", "e", "l", "l", "o"])
# print(result)
