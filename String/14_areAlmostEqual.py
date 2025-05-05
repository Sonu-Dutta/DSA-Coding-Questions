class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diffs = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diffs.append(i)

        if len(diffs) != 2:
            return False

        i, j = diffs
        return s1[i] == s2[j] and s1[j] == s2[i]


obj = Solution()
result = obj.areAlmostEqual("bank", "kanb")
print(result)  # Output: True


# class Solution:
#     def areAlmostEqual(self, s1: str, s2: str) -> bool:
#         if s1 == s2:
#             return True

#         first_diff = second_diff = -1

#         for i in range(len(s1)):
#             if s1[i] != s2[i]:
#                 if first_diff == -1:
#                     first_diff = i
#                 elif second_diff == -1:
#                     second_diff = i
#                 else:
#                     return False  # More than two differences

#         if second_diff == -1:
#             return False  # Only one mismatch → cannot swap just one character

#         return s1[first_diff] == s2[second_diff] and s1[second_diff] == s2[first_diff]
