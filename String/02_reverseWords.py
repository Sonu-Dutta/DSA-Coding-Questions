def reverseWords(s):
    return " ".join(s.strip().split()[::-1])


print(reverseWords("Reverse the words"))
