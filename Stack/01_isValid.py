
def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
            print(stack)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                print("__", mapping[char], char, stack.pop())
                return False

    return not stack


print(isValid("({[)"))
# print(isValid("({[})"))
