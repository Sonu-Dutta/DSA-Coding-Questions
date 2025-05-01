class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(string: str) -> str:
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)

        return process_string(s) == process_string(t)


res = Solution()
result = res.backspaceCompare("ab#c", "ad#c")
print(result)
