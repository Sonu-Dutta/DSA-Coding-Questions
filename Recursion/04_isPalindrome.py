class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        for i in s:
            if i.isalnum():
                a.append(i.lower())

        def helper(left, right):
            if left >= right:
                return True
            if a[left] != a[right]:
                return False
            return helper(left+1, right-1)
        return helper(0, len(a)-1)


obj = Solution()
s = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(s))
