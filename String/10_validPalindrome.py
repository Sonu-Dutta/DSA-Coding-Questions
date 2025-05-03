class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Create an empty string to store cleaned characters
        cleaned = ''

        # Step 2: Loop through each character in the string
        for c in s:
            # Step 3: If the character is a letter or a number
            if c.isalnum():
                # Step 4: Convert it to lowercase and add it to cleaned
                cleaned += c.lower()

        # Step 5: Check if the cleaned string is equal to its reverse
        reversedCleaned = cleaned[::-1]

        if cleaned == reversedCleaned:
            return True
        else:
            return False


obj = Solution()
result = obj.isPalindrome("A man, a plan, a canal: Panama")
print(result)
