from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def backtrack(index: int, path: str):
            if index == len(s):
                res.append(path)
                return

            if s[index].isalpha():
                backtrack(index + 1, path + s[index].lower())
                backtrack(index + 1, path + s[index].upper())
            else:
                backtrack(index + 1, path + s[index])

        backtrack(0, "")
        return res


obj = Solution()
print(obj.letterCasePermutation("a1b2"))  # ["a1b2","A1b2","a1B2","A1B2"]
