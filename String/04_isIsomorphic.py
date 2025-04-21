from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sToT = {}
        tToS = {}

        for charS, charT in zip(s, t):

            if charS in sToT:
                if sToT[charS] != charT:
                    return False
            else:
                sToT[charS] = charT

            if charT in tToS:
                if tToS[charT] != charS:
                    return False
            else:
                tToS[charT] = charS

        return True


sol = Solution()

print(sol.isIsomorphic("egg", "add"))
print(sol.isIsomorphic("foo", "bar"))
print(sol.isIsomorphic("paper", "title"))
