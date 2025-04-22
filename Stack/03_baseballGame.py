from collections import deque
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


sol = Solution()
result = sol.calPoints(["5", "2", "C", "D", "+"])
print(result)
