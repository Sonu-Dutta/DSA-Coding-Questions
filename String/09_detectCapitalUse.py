class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (
            word.isupper() or
            word.islower() or
            word.istitle()
        )

# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         def isUpper(c):
#             return 'A' <= c <= 'Z'

#         def isLower(c):
#             return 'a' <= c <= 'z'

#         n = len(word)
#         if n == 1:
#             return True  # One letter is always valid

#         # Case 1: All letters are uppercase
#         if all(isUpper(c) for c in word):
#             return True

#         # Case 2: All letters are lowercase
#         if all(isLower(c) for c in word):
#             return True

#         # Case 3: Only first letter uppercase, rest lowercase
#         if isUpper(word[0]) and all(isLower(c) for c in word[1:]):
#             return True

#         return False


obj = Solution()
result = obj.detectCapitalUse("CapitaL")
print(result)
