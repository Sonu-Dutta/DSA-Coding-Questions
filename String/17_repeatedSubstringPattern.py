class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        i = n // 2
        while i >= 1:
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
            i -= 1
        return False


obj = Solution()
result = obj.repeatedSubstringPattern("abababab")
print(result)  # Output: True
