class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = ""
        for char in s:
            if not char.isalnum():
                continue
            chars += char.lower()
        
        return chars == chars[::-1]