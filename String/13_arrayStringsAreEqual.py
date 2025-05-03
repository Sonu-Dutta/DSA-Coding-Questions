class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        i = j = 0
        p1 = p2 = 0

        while i < len(word1) and j < len(word2):
            c1 = word1[i][p1]
            c2 = word2[j][p2]
            print(
                f"Comparing word1[{i}][{p1}] = '{c1}' with word2[{j}][{p2}] = '{c2}'")

            if c1 != c2:
                print("Mismatch found! Returning False.")
                return False

            p1 += 1
            p2 += 1

            if p1 == len(word1[i]):
                print(f"End of word1[{i}] reached. Moving to word1[{i+1}]")
                p1 = 0
                i += 1

            if p2 == len(word2[j]):
                print(f"End of word2[{j}] reached. Moving to word2[{j+1}]")
                p2 = 0
                j += 1

        result = i == len(word1) and j == len(word2)
        print(f"End of comparison. i={i}, j={j}, result={result}")
        return result


obj = Solution()
result = obj.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])
print(result)  # Output: True
