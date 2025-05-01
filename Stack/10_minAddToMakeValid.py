class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')' and stack:
                stack.pop()
            else:
                stack.append(char)
        return len(stack)

# class Solution:
#     def minAddToMakeValid(self, s: str) -> int:
#         balance = 0
#         moves = 0

#         for c in s:
#             if c == '(':
#                 balance += 1
#             elif balance > 0:
#                 balance -= 1
#             else:
#                 moves += 1

#         return moves + balance


obj = Solution()
result = obj.minAddToMakeValid("())")
print(result)
