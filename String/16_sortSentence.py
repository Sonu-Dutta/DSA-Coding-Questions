class Solution:
    def sortSentence(self, s: str) -> str:
        w = s.split()
        res = [None] * len(w)

        for word in w:
            idx = int(word[-1])
            res[idx - 1] = word[:-1]

        ans = ' '.join(res)
        return ans


obj = Solution()
result = obj.sortSentence("is2 sentence4 This1 a3")
print(result)  # Output: "This is a sentence"
