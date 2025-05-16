from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left, right):
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            helper(left+1, right-1)

        helper(0, len(s)-1)


obj = Solution()
s = ["h", "e", "l", "l", "o"]
obj.reverseString(s)
print(s)  # Output: ['o', 'l', 'l', 'e', 'h']
