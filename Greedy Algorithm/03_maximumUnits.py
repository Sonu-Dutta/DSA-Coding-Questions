from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total = 0

        for i, j in (boxTypes):
            if truckSize == 0:
                break
            box = min(truckSize, i)
            total += box*j
            truckSize -= box
        return total


obj = Solution()
print(obj.maximumUnits([[1, 3], [2, 2], [3, 1]], 4))  # Output: 8
