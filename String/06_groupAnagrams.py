from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        anagramMap = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagramMap[key].append(word)
        # print(anagramMap)
        return list(anagramMap.values())


sol = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))
