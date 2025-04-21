class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1

            charset.add(s[right])
            maxLen = max(maxLen, right-left+1)
        return maxLen


sol = Solution()
result = sol.lengthOfLongestSubstring("pwwkew")
print(result)
