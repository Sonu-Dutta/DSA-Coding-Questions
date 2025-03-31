def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack:
                return False
            top = stack.pop()
            if mapping[char] != top:
                return False

    return not stack


print(isValid("({[})"))
