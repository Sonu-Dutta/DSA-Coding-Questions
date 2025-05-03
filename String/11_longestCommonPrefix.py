from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Sort the list
        strs.sort()

        # Compare only the first and last strings
        first = strs[0]
        last = strs[-1]
        i = 0

        # Compare characters until they mismatch
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1

        return first[:i]


obj = Solution()
result = obj.longestCommonPrefix(["flower", "flow", "flight"])
print(result)  # Output: "fl"

# Alternative approach using vertical scanning

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""

#         # Start with the prefix being the first string
#         prefix = strs[0]

#         # Compare the prefix with each string in the list
#         for string in strs[1:]:
#             # Reduce the prefix until it matches the start of the string
#             while not string.startswith(prefix):
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
#         return prefix
