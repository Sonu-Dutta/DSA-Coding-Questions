
class Solution(object):
    def arrayStringsAreEqual(self, word1: str, word2: str) -> bool:
        i = j = 0
        p1 = p2 = 0

        while i < len(word1) and j < len(word2):
            if word1[i][p1] != word2[j][p2]:
                return False

            p1 += 1
            p2 += 1

            if p1 == len(word1[i]):
                p1 = 0
                i += 1

            if p2 == len(word2[j]):
                p2 = 0
                j += 1

        return i == len(word1) and j == len(word2)


obj = Solution()
result = obj.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
print(result)  # Output: True
