from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10 and five > 0:
                five -= 1
                ten += 1

            elif five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
        return True


obj = Solution()
bills = [5, 5, 5, 10, 20]
print(obj.lemonadeChange(bills))
